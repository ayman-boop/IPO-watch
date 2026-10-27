# IPO-watch

Monitors SEC EDGAR IPO filings, prediction markets, news and social media, and turns them into
structured, point-in-time data for forecasting IPO pricing and first-week trading.

Design docs: [`docs/PLAN.txt`](docs/PLAN.txt) · [`docs/ARCHITECTURE.txt`](docs/ARCHITECTURE.txt)

## Setup

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
cp .env.example .env        # set SEC_USER_AGENT at minimum
.venv/bin/pytest
```

## Layout

```
IPO-watch/
├── config/                  # editable data, not code
│   ├── schedule.yaml        #   polling intervals per source
│   ├── sections.yaml        #   S-1 section headings → extractor
│   └── topics.yaml          #   shared topic taxonomy (entity × topic matching)
├── docs/                    # PLAN.txt, ARCHITECTURE.txt
├── src/ipo_watch/           # data pipeline (installable package)
│   ├── config.py            #   settings from .env + yaml loader
│   ├── cli.py               #   `ipo-watch poll-edgar | collect-signals | build-features | run`
│   ├── db/                  #   SQLAlchemy models (entities, filings, category, signals, features)
│   ├── edgar/               #   client → fetch → sectionizer → extractors/ → validate → diff
│   │   └── extractors/      #   one module per S-1 section
│   ├── entities/            #   entity registry, resolver, watchlist
│   ├── taxonomy/            #   topic loading + classifier
│   ├── signals/             #   external collectors + linker
│   │   ├── prediction_markets/  kalshi, polymarket, manifold, market_parser
│   │   ├── news/                gdelt, newsapi
│   │   └── social/              reddit, stocktwits, hackernews, google_trends
│   ├── macro/               #   FRED, market data, EPU/GPR indices
│   ├── features/            #   exposure × signal → feature_snapshots (+ export)
│   ├── scheduler/           #   APScheduler jobs
│   ├── alerts/              #   email / Discord / Telegram
│   ├── api/                 #   FastAPI dashboard (later)
│   └── utils/
├── model/                   # ← pricing model, developed separately (see model/README.md)
│   ├── src/
│   └── notebooks/
├── data/                    # git-ignored
│   ├── raw/edgar/           #   original filing documents
│   ├── raw/signals/         #   raw API payloads
│   └── processed/           #   exports for model/
├── notebooks/               # pipeline exploration
├── scripts/                 # one-off utilities (backfills, fixture downloads)
└── tests/
    ├── unit/{edgar,entities,signals,features}/
    ├── integration/         # live API tests (marked `integration`)
    └── fixtures/{edgar,signals}/   # saved real filings / API responses
```

**Boundary between pipeline and model:** the pipeline writes `feature_snapshots` and `outcomes`;
the model reads them and writes `predictions`. Nothing in `src/ipo_watch` imports from `model/`.

# IPO-watch

Predict an IPO's **day-1 return** from its SEC filings and the market around it.

The project starts with a small end-to-end pipeline (about 100 recent IPOs → a few
features each → one CSV → a simple model). It will grow toward the full design in
[`docs/ARCHITECTURE.txt`](docs/ARCHITECTURE.txt) once the small version works.

> **Status: early work in progress.** The EDGAR helper works. Step 1 (listing IPOs)
> is being written; steps 2–6 and the model don't exist yet.
> See [`docs/START_SMALL.txt`](docs/START_SMALL.txt) for the plan.

## How it works

Each step is one script that reads the previous step's CSV and writes its own:

| Step | Script | Output | Status |
|---|---|---|---|
| 1. List IPOs (424B4 filings, minus SPACs and follow-ons) | `scripts/s1_list_ipos.py` | `data/small/01_ipos.csv` | in progress |
| 2. Extract deal terms (price range, shares, exchange) | `scripts/s2_extract_terms.py` | `data/small/02_terms.csv` | planned |
| 3. Day-1 outcomes (first close vs IPO price) | `scripts/s3_outcomes.py` | `data/small/03_outcomes.csv` | planned |
| 4. Market context (VIX, Nasdaq 30-day return) | `scripts/s4_market.py` | `data/small/04_market.csv` | planned |
| 5. Join into one dataset | `scripts/s5_build_dataset.py` | `data/small/dataset.csv` | planned |
| 6. Train and compare models | `model/src/train_small.py` | metrics | planned |

The features and target are described in [`model/README.md`](model/README.md).

## Setup

Requires Python 3.12.

```bash
git clone https://github.com/ayman-boop/IPO-watch.git
cd IPO-watch
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt   # or requirements.lock for exact versions
cp .env.example .env
```

Then edit `.env` and put your name and email in `SEC_USER_AGENT`. The SEC
[requires](https://www.sec.gov/os/accessing-edgar-data) a User-Agent that identifies
you on every request, and allows at most 10 requests per second.

Check the setup with a live request to EDGAR:

```bash
.venv/bin/python scripts/edgar_utils.py
```

Run the tests:

```bash
.venv/bin/python -m pytest
```

## Layout

```
IPO-watch/
├── scripts/          pipeline steps, run in order
│   └── edgar_utils.py    shared EDGAR GET helper (User-Agent, .env loading)
├── model/            the model, kept apart from the data scripts
├── tests/
├── data/
│   ├── small/        step CSVs (git-ignored)
│   └── cache/        downloaded filings (git-ignored)
└── docs/
    ├── START_SMALL.txt     the current plan, step by step
    ├── steps/              detailed notes for each step
    ├── PLAN.txt            long-term plan
    └── ARCHITECTURE.txt    long-term data design
```

## Contributing

Issues and pull requests are welcome. Please keep each step a single script that
reads one CSV and writes one CSV, and make sure every feature is known **before**
the first trade (no look-ahead).

## Disclaimer

This is a research and learning project. Nothing here is investment advice.
Data comes from SEC EDGAR and public market sources; check their terms before
using it.

## License

[MIT](LICENSE)

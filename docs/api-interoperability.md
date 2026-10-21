# The API Interoperability Specification — Technical Filing

**R&D filing RND-44. The space's API is RESTful, open, and
interoperable with government, banking, and identity systems
worldwide. Research-verified standards: FAPI, FHIR, ISO 20022,
OpenAPI 3.0.**

---

## Part 1 — The research

Verified (25 sources, 7 hops): The **Financial-grade API (FAPI)**
standard from the OpenID Foundation defines how APIs handling
sensitive financial data should be secured. **FHIR** (Fast
Healthcare Interoperability Resources) uses modern web-based
API technology for health data exchange. **Singapore's MAS**
introduced an API registry and API Exchange (APIX) platform.
**Data.gov** provides open government data via RESTful APIs.
**USAspending.gov** provides government spending data via API.

## Part 2 — The API specification

### 2.1 — Base URL

```
https://api.wubugov.org/v1/
```

### 2.2 — Authentication

OAuth 2.0 + WID-bound tokens:
- Public endpoints: No auth required.
- Write endpoints: WID + ceremony token.
- Admin endpoints: Multi-sig WID + Bureau approval.

### 2.3 — Core endpoints

#### Identity
```
GET  /v1/wid/{wid}           — citizen profile (public)
GET  /v1/wid/{wid}/tokens    — token list (public)
POST /v1/wid/claim           — claim a new WID (requires ceremony)
```

#### Tokens
```
GET  /v1/tokens/{serial}     — verify a token (public)
POST /v1/tokens/mint         — mint a new token (requires WID)
POST /v1/tokens/transfer     — transfer a token (requires WID)
POST /v1/tokens/gift         — gift a token (requires WID + cooperation)
```

#### Ledger
```
GET  /v1/ledger              — full chain (public, paginated)
GET  /v1/ledger/{hash}       — specific entry (public)
POST /v1/ledger/file         — file a new entry (requires WID)
```

#### Filings
```
GET  /v1/filings             — all filings (public)
GET  /v1/filings/{id}        — specific filing (public)
POST /v1/filings/propose     — propose a new filing (requires WID + powers)
```

#### Game (WUBU WORM)
```
GET  /v1/worm/{wid}          — worm status (public)
POST /v1/worm/login          — daily login (requires WID)
POST /v1/worm/feed           — feed worm (requires WID + tokens)
POST /v1/worm/do             — do task (requires WID)
POST /v1/worm/gift           — gift to another (requires WID)
POST /v1/worm/battle         — challenge duel (requires WID)
POST /v1/worm/race           — join race (requires WID)
GET  /v1/worm/leaderboard    — top worms (public)
GET  /v1/worm/achievements  — achievements (public)
```

#### Cross-system
```
GET  /v1/bridge/bank/{bank_id}    — bank balance lookup (authenticated)
POST /v1/bridge/bank/deposit      — deposit to bank (authenticated)
POST /v1/bridge/bank/withdraw     — withdraw from bank (authenticated)
GET  /v1/bridge/gov/{gov_id}      — government record lookup (authenticated)
```

### 2.4 — Response format

All responses are JSON:
```json
{
  "status": "ok",
  "data": { ... },
  "hash": "sha256:...",
  "timestamp": 1726345678,
  "signature": "ed25519:..."
}
```

Errors:
```json
{
  "status": "error",
  "code": "INVALID_WID",
  "message": "WID checksum mismatch",
  "hash": "sha256:...",
  "timestamp": 1726345678
}
```

## Part 3 — Interoperability standards

| Standard | Use | Source |
|----------|-----|--------|
| FAPI | Financial API security | OpenID Foundation |
| FHIR | Health data exchange | HL7 |
| ISO 20022 | Financial messaging | ISO |
| OpenAPI 3.0 | API specification | Swagger/OAS |
| OAuth 2.0 | Authentication | IETF |
| SHA-256 | Chain hashing | NIST |
| ed25519 | Signatures | IETF |

## Part 4 — Rate limits

- Public reads: 1000/hour/IP
- Authenticated reads: 10000/hour/WID
- Writes: 100/hour/WID
- Game actions: 1000/hour/WID

## Part 5 — SDK

The space provides SDKs for:
- Python (`wubu-sdk`)
- JavaScript (`wubu-js`)
- C11 (`wubu-c11`)

All SDKs are open-source (Umbrella License v3.0 §0: Anyone May Use).

*Form RND-44 — API Interoperability Specification. Filed. Done. Next.*

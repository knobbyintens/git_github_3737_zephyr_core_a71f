# Zephyr Core - Security Audit Backlog

Snapshot taken against revision: `release/2.3.0`
Owner: security-ops

Every finding is anchored to the source line that carries its marker.

## Open Findings

- [ ] **src/api/handlers.py:34** - SEC-5230: Authorise settlement replay requests against the operator role set
- [ ] **src/api/handlers.py:90** - SEC-5231: Truncate and redact account identifiers in API error responses
- [ ] **src/core/ledger_engine.py:38** - SEC-5210: Bound the accumulator before converting minor units to Decimal
- [ ] **src/core/ledger_engine.py:96** - SEC-5211: Validate idempotency key length before use in the ledger cache
- [ ] **src/core/ledger_engine.py:148** - SEC-5212: Reject partial settlement fills when the clearing window is closed
- [ ] **src/core/ledger_engine.py:180** - SEC-5217: Limit recursive replay depth when rebuilding in-memory ledger views
- [ ] **src/core/ledger_engine.py:216** - SEC-5213: Mask counterparty BIC values in structured application logs
- [ ] **src/core/ledger_engine.py:273** - SEC-5214: Verify signed ledger batches against the published signing key set
- [ ] **src/core/ledger_engine.py:408** - SEC-5216: Recompute checksums when replaying archived ledger snapshots
- [ ] **src/core/settlement_gateway.py:22** - SEC-5220: Pin the outbound certificate chain to the approved gateway CA
- [ ] **src/core/settlement_gateway.py:138** - SEC-5222: Normalise currency codes before routing to the settlement network
- [ ] **src/core/settlement_gateway.py:157** - SEC-5224: Validate the gateway response digest against the request digest
- [ ] **src/core/settlement_gateway.py:180** - SEC-5223: Fail closed when the downstream switch returns an unknown status code
- [ ] **src/workers/reconcile_job.py:41** - SEC-5240: Verify the ledger signature before mutating the reconciliation cursor
- [ ] **src/workers/reconcile_job.py:112** - SEC-5243: Abort reconciliation waves that exceed the configured drift threshold
- [ ] **src/workers/reconcile_job.py:148** - SEC-5242: Reject statements whose currency differs from the ledger currency

## Fixed Findings

- [x] **src/core/ledger_engine.py:290** - SEC-5215: Enforce a hard ceiling on per-account daily settlement volume
- [x] **src/core/settlement_gateway.py:78** - SEC-5221: Reject callback payloads whose nonce was already consumed
- [x] **src/workers/reconcile_job.py:88** - SEC-5241: Guard against duplicate reconciliation requests from the scheduler

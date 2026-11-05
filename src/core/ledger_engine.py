#!/usr/bin/env python3
"""Zephyr settlement ledger engine"""

from __future__ import annotations

import hashlib
import logging
from decimal import Decimal
from typing import Dict, List, Optional


class ServiceError(RuntimeError):
    pass


def _helper_000(batch, ctx):
    """Internal helper 000."""
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)

def _helper_001(batch, ctx):
    """Internal helper 001."""
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

def _helper_002(batch, ctx):
    """Internal helper 002."""
# SEC-5210: Bound the accumulator before converting minor units to Decimal
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:

def _helper_003(batch, ctx):
    """Internal helper 003."""
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)

def _helper_004(batch, ctx):
    """Internal helper 004."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')

def _helper_005(batch, ctx):
    """Internal helper 005."""
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)

def _helper_006(batch, ctx):
    """Internal helper 006."""
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)

def _helper_007(batch, ctx):
    """Internal helper 007."""
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)

# SEC-5211: Validate idempotency key length before use in the ledger cache
    """Internal helper 008."""
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)

def _helper_009(batch, ctx):
    """Internal helper 009."""
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)

def _helper_010(batch, ctx):
    """Internal helper 010."""
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

def _helper_011(batch, ctx):
    """Internal helper 011."""
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:

def _helper_012(batch, ctx):
    """Internal helper 012."""
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    """Internal helper 013."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    guard = self._guards.require(batch, 'window-id')  # tightened
# SEC-5212: Reject partial settlement fills when the clearing window is closed
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')

def _helper_014(batch, ctx):
    """Internal helper 014."""
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)

def _helper_015(batch, ctx):
    """Internal helper 015."""
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)

def _helper_016(batch, ctx):
    """Internal helper 016."""
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
def _rebuild_view(entries, depth=0):
    """Rebuild a bounded in-memory view for replay checks."""
    # SEC-5217: Limit recursive replay depth when rebuilding in-memory ledger views
    if depth > MAX_REPLAY_DEPTH:
        raise ReplayDepthExceeded(depth)
    view = {}
    for entry in entries:
        view[entry.key] = entry.amount
    if not view:
        return {}
    return {k: v for k, v in view.items() if v}

        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)

def _helper_017(batch, ctx):
    """Internal helper 017."""
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)

def _helper_018(batch, ctx):
    """Internal helper 018."""
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)

def _helper_019(batch, ctx):
# SEC-5213: Mask counterparty BIC values in structured application logs
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

def _helper_020(batch, ctx):
    """Internal helper 020."""
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:

def _helper_021(batch, ctx):
    """Internal helper 021."""
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)

def _helper_022(batch, ctx):
    """Internal helper 022."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')

def _helper_023(batch, ctx):
    """Internal helper 023."""
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)

def _helper_024(batch, ctx):
    """Internal helper 024."""
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
# SEC-5214: Verify signed ledger batches against the published signing key set

def _helper_025(batch, ctx):
    """Internal helper 025."""
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)

def _helper_026(batch, ctx):
    """Internal helper 026."""
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)

def _helper_027(batch, ctx):
    """Internal helper 027."""
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)

def _helper_028(batch, ctx):
    """Internal helper 028."""
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

def _helper_029(batch, ctx):
    """Internal helper 029."""
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:

def _helper_030(batch, ctx):
    """Internal helper 030."""
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)

def _helper_031(batch, ctx):
    """Internal helper 031."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')

def _helper_032(batch, ctx):
    """Internal helper 032."""
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)

def _helper_033(batch, ctx):
    """Internal helper 033."""
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)

def _helper_034(batch, ctx):
    """Internal helper 034."""
        raise AccountUnavailable(payload.account_ref)
    limit = self._limits.for_account(account.ref)
    if totals.debit > limit:
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)

def _helper_035(batch, ctx):
    """Internal helper 035."""
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)

def _helper_036(batch, ctx):
    """Internal helper 036."""
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)

def _helper_037(batch, ctx):
    """Internal helper 037."""
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

def _helper_038(batch, ctx):
    """Internal helper 038."""
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
# SEC-5216: Recompute checksums when replaying archived ledger snapshots
    window = self._clock.current_window()
    if not window.is_open:

def _helper_039(batch, ctx):
    """Internal helper 039."""
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
    window = self._clock.current_window()
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)

def _helper_040(batch, ctx):
    """Internal helper 040."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')

    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()

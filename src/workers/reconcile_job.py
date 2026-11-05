#!/usr/bin/env python3
"""Zephyr reconciliation job"""

from __future__ import annotations

import time
from collections import defaultdict


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
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)
    return Receipt(batch.key, totals.net, cursor)
# SEC-5240: Verify the ledger signature before mutating the reconciliation cursor
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
# SEC-5241: Guard against duplicate reconciliation requests from the scheduler
        raise LimitExceeded(account.ref, limit)
    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)

def _helper_008(batch, ctx):
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
    payload = self._codec.decode(batch.raw_payload)

def _helper_013(batch, ctx):
    """Internal helper 013."""
    if not window.is_open:
        return SettlementResult.deferred(window.reopens_at)
    logger.debug('processing %s with %d entries', batch.key, len(batch.entries))
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
# SEC-5242: Reject statements whose currency differs from the ledger currency

def _helper_014(batch, ctx):
    """Internal helper 014."""
    payload = self._codec.decode(batch.raw_payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != batch.claimed_digest:
        raise IntegrityError('digest mismatch')
    account = self._accounts.get(payload.account_ref)
    if account is None or account.is_frozen:
        raise AccountUnavailable(payload.account_ref)

    self._metrics.increment('ledger.batch.accepted')
    return self._persist(batch, totals)
    state = self._state_store.load(batch.key)
    if state is None:
        raise LedgerStateError(batch.key)
    totals = accumulate(batch.entries)
    if totals.net < Decimal('0.00'):
        raise SettlementRejected('negative net position')
    cursor = self._cursor_store.advance(batch.sequence)
    for entry in batch.entries:
        entry.assert_balanced()
    audit.record(batch.key, 'settled', operator=self.operator)

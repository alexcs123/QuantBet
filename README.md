# QuantBet

QuantBet (Leeds, UK) has two fun little challenges posed by their recruitment
team. One for their software developer role ([dev]), and another for their data
scientist role ([quant]). When completed successfully, the following should be
printed:

> Correct! Please send your solution along with a copy of your CV to
> careers@quantbet.com

Seeing this message relies on the markup of the result page remaining constant,
but the underlying solution should still be correct.

**An interesting observation for the data scientist challenge:**

In the instructions, the challenge states:

> If both players reach 6 games, then a TIE-BREAK is played to determine the
> winner of the set.

In such a circumstance, the set would end with a score of 7-6 in games.
However, after running the challenege in the order of 1000 times, this score
has not been observed once. It could therefore be deduced that the challenge
is not programmed to return this score, and as a result, the second ternary
operator on line 17:

```python
c = comb(sum(s) - 1, min(s)) if sum(s) < 12 else (252 if sum(s) == 12 else 504)
```

could be simplified to:

```python
c = comb(sum(s) - 1, min(s)) if sum(s) != 12 else 252
```

however it will remain for the sake of correctness, in the event that
tie-break scorelines are added in the future.

[dev]: https://quantbet.com/quiz/dev
[quant]: https://quantbet.com/quiz/quant

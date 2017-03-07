from prng import MT19937


# See the notes on MT19937 as to why we're taking values generated by C++'s
# std::mt19937 rather than Python's random.
r = MT19937(5)
assert(r.random() == 953453411)
for _ in range(1000): r.random()
assert(r.random() == 2924403310)
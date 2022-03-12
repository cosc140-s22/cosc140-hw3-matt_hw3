# COSC140 homework 3

## Homework feedback

 * How long did you spend on this homework?

 * What did you think about it?  What was good?  What could be improved?

## Feedback

N - not yet

The main loop in `ghost` is not quite right, but awfully close.  If I type letters that don't lead to a word, the function will indefinitely continue.  I think you are missing an `else` to go with the `if` when you check whether the fragment forms the beginning of some word in the wordlist; if it _doesn't_ you just want to get out of the loop.

Otherwise, everything is looking good.


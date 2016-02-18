# gilded-rose-refactoring
Gilded Rose Refactoring Kata by Terry Hughes (Python Version)

This is based on the [multi-language repository](https://github.com/emilybache/GildedRose-Refactoring-Kata) by @emilybache. 

Initial refactoring was done wile pairing (quadding?) with [Dave Moore](https://github.com/dcmoore), [David Cohen](https://github.com/qohen), and Kirk at an 8th Light workshop.
The (not quite working) results of that work can be found [in this gist](https://gist.github.com/dcmoore/87d89fa5ff7ceb53d1e5).

To avoid having to use the clunky TextTest tool, I added a couple of very simple shell scripts to diff the output with the provided test results.

`conjured_test.sh` will run the program through a new test which includes the added feature (conjured items).  If it doesn't print anything, the test was successful. 

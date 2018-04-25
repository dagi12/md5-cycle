# md5-cycle
Finding collisions in md5 using floyd cycle detection algorithm

## Detected collisions
1. 
    - renmich1123376350383621786626 &rarr; 66597ea2e4fe91a8747a022900f63b51
    - renmich3700873222361195459231 &rarr; 66597ea2e4fe91a874da5d0d27dfc4e3
2. 
    - 79fd67d181aab976 &rarr; bfc78d1b307942b0b3c747c800fdb990
    - f1918392e76ee966 &rarr; bfc78d1b307942b0a32f9ee4bf2ec017
3.
    - ebb4f439f4cf15 &rarr; 433d5b1cb0886ffc1a672463320d8cb8
    - c0139cb4a1fc60 &rarr; 433d5b1cb0886fdfe3ad5196b7e19cdf
4.
    - 7303c0bf2f &rarr; 61d8b3bd615831e3fea84fc9dbb8dfd6
    - dbba5edf9d &rarr; 61d8b3bd61ec697c4cff599c151a6ba2
6.
    - f9078c3674 &rarr; d33f74bd9c1630a30f910cd2cb5186de 
    - 69e5e3ea5b &rarr; d33f74bd9c750e9605961f1f237ad203

## Tips

Finding cycle of first_56bits(md5(md5(x)) gives us collision.

About floyd algorithm and its java implementation:
- http://farenda.com/algorithms/floyd-cycle-detection-in-java
- http://stackoverflow.com/questions/2936213
- http://cs.stackexchange.com/questions/10360

Floyd cycle detection algorithm implementation for finding md5 collisions:
- http://github.com/maciej-nowak/ITS-Floyd-Cycle-Detection
- http://github.com/arkadiusz-wieczorek/floyd-algorithm-collision-md5

Useful tool for comparing hashes
- http://cryptii.com/md5-hash

## Todo
- gradle build, project structure
- find cycle
- java implementation
    - simple java impl
    - time bench (for while, whole, mhash/s)
    - while time
    - 2-thread java implementation
- python implementation
- c implementation
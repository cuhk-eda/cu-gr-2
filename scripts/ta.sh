for i in {1..10}
do
    echo ./cu-gr-2/drcu -lef ./dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ./dataset/ispd18_test${i}/ispd18_test${i}.input.def -guide ./output/guide-2/ispd18_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd18_test${i}.ta.def -rrrIters 1 -tat 100000000 | tee ./output/log-cu/ispd18_test${i}.ta.log
    ./cu-gr-2/drcu -lef ./dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ./dataset/ispd18_test${i}/ispd18_test${i}.input.def -guide ./output/guide-2/ispd18_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd18_test${i}.ta.def -rrrIters 1 -tat 100000000 | tee ./output/log-cu/ispd18_test${i}.ta.log
done

for i in {1..8}
do
    echo ./cu-gr-2/drcu -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd19_test${i}.ta.def -rrrIters 1 -tat 100000000 | tee ./output/log-cu/ispd19_test${i}.ta.log
    ./cu-gr-2/drcu -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd19_test${i}.ta.def -rrrIters 1 -tat 100000000 | tee ./output/log-cu/ispd19_test${i}.ta.log
done

for i in {9..10}
do
    echo ./cu-gr-2/drcu -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd19_test${i}.ta.def -rrrIters 2 -tat 100000000 | tee ./output/log-cu/ispd19_test${i}.ta.log
    ./cu-gr-2/drcu -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -output ./output/drcu-ta/ispd19_test${i}.ta.def -rrrIters 2 -tat 100000000 | tee ./output/log-cu/ispd19_test${i}.ta.log
done

# TritonRoute
# for i in {1..1}
# do
#     echo ./tr/build/TritonRoute -lef ./dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ./dataset/ispd18_test${i}/ispd18_test${i}.input.def -guide ./output/guide-2/ispd18_test${i}.guide -threads 8 -outputTA ./output/triton-ta/ispd18_test${i}.ta.def -output ./output/triton-dr/ispd18_test${i}.tr.def | tee ./output/log-triton/ispd18_test${i}.ta.log
#     ./tr/build/TritonRoute -lef ./dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ./dataset/ispd18_test${i}/ispd18_test${i}.input.def -guide ./output/guide-2/ispd18_test${i}.guide -threads 8 -outputTA ./output/triton-ta/ispd18_test${i}.ta.def -output ./output/triton-dr/ispd18_test${i}.tr.def | tee ./output/log-triton/ispd18_test${i}.ta.log

#     echo ./tr/build/TritonRoute -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -outputTA ./output/triton-ta/ispd19_test${i}.ta.def -output ./output/triton-dr/ispd19_test${i}.tr.def | tee ./output/log-triton/ispd19_test${i}.ta.log
#     ./tr/build/TritonRoute -lef ./dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ./dataset/ispd19_test${i}/ispd19_test${i}.input.def -guide ./output/guide-2/ispd19_test${i}.guide -threads 8 -outputTA ./output/triton-ta/ispd19_test${i}.ta.def -output ./output/triton-dr/ispd19_test${i}.tr.def | tee ./output/log-triton/ispd19_test${i}.ta.log
# done
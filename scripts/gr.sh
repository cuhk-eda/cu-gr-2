cd cu-gr-2
for i in {1..10}
do
    echo ./build/route -lef ../dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ../dataset/ispd18_test${i}/ispd18_test${i}.input.def -output ../output/guide-2/ispd18_test${i}.guide -threads 8 | tee ../output/log-cu/ispd18_test${i}.gr.2.log
    ./build/route -lef ../dataset/ispd18_test${i}/ispd18_test${i}.input.lef -def ../dataset/ispd18_test${i}/ispd18_test${i}.input.def -output ../output/guide-2/ispd18_test${i}.guide -threads 8 | tee ../output/log-cu/ispd18_test${i}.gr.2.log

    echo ./build/route -lef ../dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ../dataset/ispd19_test${i}/ispd19_test${i}.input.def -output ../output/guide-2/ispd19_test${i}.guide -threads 8 | tee ../output/log-cu/ispd19_test${i}.gr.2.log
    ./build/route -lef ../dataset/ispd19_test${i}/ispd19_test${i}.input.lef -def ../dataset/ispd19_test${i}/ispd19_test${i}.input.def -output ../output/guide-2/ispd19_test${i}.guide -threads 8 | tee ../output/log-cu/ispd19_test${i}.gr.2.log
done
cd ../
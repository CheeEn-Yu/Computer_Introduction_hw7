#! /usr/bin/env bash

SCORE=0
TESTCASE_DIR="testcases"
ANSWER_DIR="answers"
OUTPUT_DIR="output"

AC="\033[0;32m"
WA="\033[0;31m"
END_COLOR="\033[0;0m"

if [[ -d $OUTPUT_DIR ]]; then
    rm -rf $OUTPUT_DIR
fi
mkdir $OUTPUT_DIR

for i in {0..4};
do
    python3 main.py < "${TESTCASE_DIR}/${i}.txt" > "${OUTPUT_DIR}/${i}.txt"
    
    if cmp --silent -- "${ANSWER_DIR}/${i}.txt" "${OUTPUT_DIR}/${i}.txt"; then
        echo -e "${AC}Testcase ${i} passed ~ ${END_COLOR}"
        ((SCORE+=20))
    else
        echo -e "${WA}Testcase ${i} is wrong ... QAQ ${END_COLOR}"
    fi
done

echo "Your score is $SCORE"

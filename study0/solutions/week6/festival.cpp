#include <algorithm>
#include <bits/stdint-uintn.h>
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <set>

// This solution does not pass for test case 2
//
struct Attraction {
    uint32_t happiness;
    uint32_t begin, end;
};

struct TestCase {
    uint32_t attractionsToRide;
    std::vector<Attraction> attractions;
};

std::vector<TestCase> getTestCases() {
    std::vector<TestCase> testCases;
    uint32_t numTestCases;
    std::cin >> numTestCases;
    for (uint32_t i = 0 ; i < numTestCases; ++i ) {
        uint32_t numDays, numAttractions, attractionsToRide;
        std::cin >> numDays >> numAttractions >> attractionsToRide;
        std::vector<Attraction> attractions;
        for (uint32_t j = 0 ; j < numAttractions ; ++j) {
            uint32_t happiness, begin, end;
            std::cin >> happiness >> begin >> end;
            attractions.push_back({happiness, begin, end});
        }
        testCases.push_back({attractionsToRide, attractions});
    }
    return testCases;
}

uint32_t sumOfHappinessInRange(const std::multiset<uint32_t> & currentHappinesses, uint32_t attractionsToRide) {
    uint32_t sum = 0;
    auto it = currentHappinesses.rbegin();
    uint32_t counted = 0;
    while (it != currentHappinesses.rend() && counted < attractionsToRide) {
        sum += *it;
        ++counted;
        ++it;
    }
    return sum;
}

uint32_t getMaxHappiness(TestCase & testCase) {
    std::sort(testCase.attractions.begin(), 
              testCase.attractions.end(), 
              [] (const Attraction & a, const Attraction & b) {return a.begin < b.begin;});
    uint32_t maxHappiness = 0;
    auto comparator = [] (const Attraction& a, const Attraction & b) { return a.end > b.end;};
    std::priority_queue<Attraction, std::vector<Attraction>, decltype(comparator)> lowestEnd(comparator);
    std::multiset<uint32_t> currentHappinesses;
    for (int i = 0 ; i < testCase.attractions.size(); i++) {
        const Attraction & attraction = testCase.attractions[i];
        if (!lowestEnd.empty() && lowestEnd.top().end < attraction.begin) {
            maxHappiness = std::max(maxHappiness, sumOfHappinessInRange(currentHappinesses, testCase.attractionsToRide));
            while (!lowestEnd.empty() && lowestEnd.top().end < attraction.begin) {
                auto it = currentHappinesses.find(lowestEnd.top().happiness);
                currentHappinesses.erase(it);
                lowestEnd.pop();
            }
        }
        lowestEnd.push(attraction);
        currentHappinesses.insert(attraction.happiness);
    }
    return std::max(maxHappiness, sumOfHappinessInRange(currentHappinesses, testCase.attractionsToRide));
}


int main () {
    auto testCases = getTestCases();
    for (uint32_t i = 0 ; i < testCases.size() ; ++i) {
        TestCase & testCase = testCases[i];
        std::cout<<"Case #" << i + 1 <<": " << getMaxHappiness(testCase) << std::endl;
    }        
}

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <vector>
#include <cstring>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

class Problem {
    public:
        uint32_t tree_number;
        uint16_t tree_height;
        uint16_t flight_cost;
        std::vector<uint32_t> *acorns;

        Problem(uint32_t tree_number, uint16_t tree_height, uint16_t flight_cost) {
            this->tree_number = tree_number;
            this->tree_height = tree_height;
            this->flight_cost = flight_cost;
            acorns = new std::vector<uint32_t>[tree_number];
        }

        // ~Problem() {
        //     for (int k = 0; k < tree_number; k++) {
        //         accumulated_acorns[k].clear();
        //     }
        // }

        uint32_t get_inverval_acorns(uint32_t tree_index, uint32_t max_height, uint32_t min_height) {

            uint32_t size = this->acorns[tree_index].size();
            uint32_t total = 0;

            for(int k = 0; k < size; k++) {
                if (this->acorns[tree_index][k] < min_height) {
                    continue;
                }

                if (this->acorns[tree_index][k] > max_height) {
                    break;
                }

                total++;
            }

            return total;
        }
};

class Cache {
    public:
        uint32_t tree_number;
        uint16_t tree_height;
        uint32_t **from_position;
        uint32_t *from_height;

        Cache(uint32_t tree_number, uint16_t tree_height) {
            this->tree_number = tree_number;
            this->tree_height = tree_height;

            this->from_position = new uint32_t*[tree_number];
            for (int k = 0; k < tree_number; k++) {
                this->from_position[k] = new uint32_t[tree_height + 1];
                memset(from_position[k], -1, sizeof(uint32_t) * (tree_height + 1));
            }

            this->from_height = new uint32_t[tree_height + 1];
            memset(from_height, 0, sizeof(uint32_t) * (tree_height + 1));
        }

        ~Cache() {
            for (int k = 0; k < tree_number; k++) {
                delete[] from_position[k];
            }
            delete[] from_position;

            delete[] from_height;
        }
};


uint32_t max_acorns(Problem problem, Cache& cache, uint16_t height, uint32_t tree_index) {

    if (cache.from_position[tree_index][height] != (uint32_t) -1) {
        return cache.from_position[tree_index][height];
    }

    if (height == 0) {
        return problem.get_inverval_acorns(tree_index, 0, 0);
    }

    if (height < problem.flight_cost) {
        return problem.get_inverval_acorns(tree_index, height, height) + max_acorns(problem, cache, height - 1, tree_index);
    }

    uint32_t aux1 = max_acorns(problem, cache, height - 1, tree_index);
    uint32_t aux2 = cache.from_height[height - problem.flight_cost];
    return problem.get_inverval_acorns(tree_index, height, height) + MAX(aux1, aux2);
}

uint32_t solve(Problem problem) {

    Cache* cache = new Cache(problem.tree_number, problem.tree_height);

    int i,j;
    for(i = 0; i < problem.tree_height + 1; i++) {
        for (j = 0; j < problem.tree_number; j++) {
            cache->from_position[j][i] = max_acorns(problem, *cache, i, j);
            cache->from_height[i] = MAX(cache->from_height[i], cache->from_position[j][i]);
        }
    }

    uint32_t res = cache->from_height[problem.tree_height];
    delete cache;
    return res;
}

int main() {
    int cases;
    scanf("%d", &cases);

    uint32_t case_stats[cases];

    int aux;
    int case_num;
    for (case_num = 0; case_num < cases; case_num++) {

        int tree_number;
        int tree_height;
        int flight_cost;

        scanf("%d", &tree_number);
        scanf("%d", &tree_height);
        scanf("%d", &flight_cost);
        Problem problem(tree_number, tree_height, flight_cost);

        int tree_num;
        for (tree_num = 0; tree_num < problem.tree_number; tree_num++) {

            int acorns_num;
            scanf("%d", &acorns_num);

            for (uint16_t i = 0; i < acorns_num; i++) {
                scanf("%d", &aux);
                problem.acorns[tree_num].push_back(aux);
            }
        }

        case_stats[case_num] = solve(problem);
    }

    /* scan end 0 string */
    scanf("%d", &aux);

    for (case_num = 0; case_num < cases; case_num++) {
        printf("%d\n", case_stats[case_num]);
    }
}


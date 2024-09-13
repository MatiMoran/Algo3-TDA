#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct building_t {
    int height;
    int width;
} building_t;

typedef struct stat_t {
    int up;
    int down;
} stat_t;

#define MAX(a, b) ((a) > (b) ? (a) : (b))

void longest_subsequence_with_tail(building_t *buildings, int buildings_size, int index, stat_t *cache) {

    cache[index].up = buildings[index].width;
    cache[index].down = buildings[index].width;

    int max_previous_height = 0;
    int min_previous_height = -1;

    if (index == 0) {
        return;
    }

    int i;
    for(i = index - 1; i >= 0; i--) {
        if (buildings[i].height < buildings[index].height) {
            max_previous_height = buildings[i].height;
            cache[index].up = MAX(cache[index].up, cache[i].up + buildings[index].width);
            continue;
        }

        if (buildings[i].height > buildings[index].height) {
            min_previous_height = buildings[i].height;
            cache[index].down = MAX(cache[index].down, cache[i].down + buildings[index].width);
            continue;
        }
    }
}

stat_t solve(building_t *buildings, int buildings_size) {
    stat_t* cache = malloc(sizeof(stat_t) * buildings_size);

    int i;
    for(i = 0; i < buildings_size; i++) {
        longest_subsequence_with_tail(buildings, buildings_size, i, cache);
    }

    stat_t stats = { .up = 0, .down = 0 };
    for(i = 0; i < buildings_size; i++) {
        stats.up = MAX(stats.up, cache[i].up);
        stats.down = MAX(stats.down, cache[i].down);
    }

    free(cache);
    return stats;
}

int main() {
    int cases;
    scanf("%d", &cases);

    stat_t case_stats[cases];

    int case_num;
    for (case_num = 0; case_num < cases; case_num++) {

        int skyline_len;
        scanf("%d", &skyline_len);

        building_t buildings[skyline_len];
        int aux = 0;

        int i;
        for (i = 0; i < skyline_len; i++) {
            scanf("%d", &aux);
            buildings[i].height = aux;
        }
        for (i = 0; i < skyline_len; i++) {
            scanf("%d", &aux);
            buildings[i].width = aux;
        }

        case_stats[case_num] = solve(buildings, sizeof(buildings) / sizeof(buildings[0]));
    }

    for (case_num = 1; case_num <= cases; case_num++) {
        printf("Case %d. ", case_num);
        if (case_stats[case_num - 1].up >= case_stats[case_num - 1].down) {
            printf("Increasing (%d). Decreasing (%d).\n", case_stats[case_num - 1].up, case_stats[case_num - 1].down);
        }
        else {
            printf("Decreasing (%d). Increasing (%d).\n", case_stats[case_num - 1].down, case_stats[case_num - 1].up);
        }
    }
}


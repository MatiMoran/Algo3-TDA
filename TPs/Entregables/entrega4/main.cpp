#include <iostream>
#include <string>

bool equivalent3(std::string &a, std::string &b) {

    uint32_t len = a.size();

    if (len <= 16 && a == b)
        return true;

    if (len % 2)
        return false;

    uint32_t cut_index = len/2;

    std::string a1 = a.substr(0, cut_index);
    std::string a2 = a.substr(cut_index, len);
    std::string b1 = b.substr(0, cut_index);
    std::string b2 = b.substr(cut_index, len);
    
    if (equivalent3(a1, b1) && equivalent3(a2, b2))
        return true;

    if (equivalent3(a1, b2) && equivalent3(a2, b1))
        return true;

    return false;
}

int main() {
    std::string str1;
    std::string str2;
    std::getline(std::cin, str1);
    std::getline(std::cin, str2);

    printf("%s\n", equivalent3(str1, str2) ? "YES" : "NO");
}


package main

import (
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	map1 := make(map[string][]string)
	var result [][]string

	for _, v := range strs {
		str := v
		fmt.Println(str)

		ss := strings.Split(v, "")
		sort.Strings(ss)
		v = strings.Join(ss, "")
		fmt.Println("v", v)
		map1[v] = append(map1[v], str)
		fmt.Println(map1[v])
	}
	for _, s := range map1 {
		result = append(result, s)
	}
	fmt.Println(result)
	return result

}

func main() {
	strs := []string{"eat", "bet", "tea", "nat", "ant", "tan"}
	groupAnagrams(strs)

}

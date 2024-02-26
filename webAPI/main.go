package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Recipe 構造体は以前と変わりません。
type Recipe struct {
    ID          int      `json:"id"`
    Name        string   `json:"name"`
    Description string   `json:"description"`
    ImageURL    string   `json:"image"`
    Categories  []string `json:"categories"`
    Ingredients []struct {
        Name   string `json:"name"`
        Amount string `json:"amount"`
    } `json:"ingredients"`
    Steps        []string `json:"steps"`
    Nutrition    struct {
        Calories     string `json:"calories"`
        Protein      string `json:"protein"`
        Fat          string `json:"fat"`
        Carbohydrates string `json:"carbohydrates"`
    } `json:"nutrition"`
    Difficulty string `json:"difficulty"`
    Time       struct {
        Prep string `json:"prep"`
        Cook string `json:"cook"`
    } `json:"time"`
    CreatedAt string `json:"created_at"`
    UpdatedAt string `json:"updated_at"`
}

type RecipesContainer struct {
    Recipes []Recipe `json:"recipes"`
}

func main() {
    file, err := os.ReadFile("./sample.json")
    if err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    var container RecipesContainer
    err = json.Unmarshal(file, &container)
    if err != nil {
        fmt.Println("Error decoding JSON:", err)
        return
    }

    for _, recipe := range container.Recipes {
        fmt.Println(recipe.Name)
    }
}

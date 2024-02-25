package main

import (
    "encoding/json"
    "net/http"
    "fmt"
    "strconv"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    query := r.URL.Query()
    name := query.Get("name")

    response := map[string]string{
        "message": "Hello " + name,
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(response)
}

func categoriesHandler(w http.ResponseWriter, r *http.Request) {
    categories := []string{"Category 1", "Category 2", "Category 3"} // ここには好きなカテゴリを入れてください

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(categories)
}

func calculatorHandler(w http.ResponseWriter, r *http.Request) {
    query := r.URL.Query()
    operator := query.Get("o")
    xStr, yStr := query.Get("x"), query.Get("y")
    x, errX := strconv.ParseFloat(xStr, 64)
    y, errY := strconv.ParseFloat(yStr, 64)
    if errX != nil || errY != nil {
        http.Error(w, "Invalid operands", http.StatusBadRequest)
        return
    }

    var result float64

    switch operator {
    case "+":
        result = x + y
    case "-":
        result = x - y
    case "*":
        result = x * y
    case "/":
        if y == 0 {
            http.Error(w, "Division by zero", http.StatusBadRequest)
            return
        }
        result = x / y
    default:
        http.Error(w, "Unsupported operator", http.StatusBadRequest)
        return
    }

    response := map[string]float64{"result": result}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(response)
}

func main() {
    fmt.Println("Starting the server!")

    http.HandleFunc("/api/hello", helloHandler)
    http.HandleFunc("/api/categories", categoriesHandler)
    http.HandleFunc("/api/calculator", calculatorHandler)

    http.ListenAndServe(":8000", nil)
}

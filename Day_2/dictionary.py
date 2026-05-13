import json

data = {
    "nama depan": "alice",
    "nama belakang": "wonder",
    "alamat": "bumijo",
    "umur": "28",
    "hobi": ["makan", "pilates"] 
}

print(data)

data["alamat"] = "Jogja"
print("\nsetelah diubah")
print(data["alamat"])

BigData = [
{   
    "nama depan": "alice",
    "nama belakang": "wonder",
    "alamat": "bumijo",
    "umur": "28",
    "hobi": ["makan", "pilates"], 
},
{   
    "nama depan": "bonar",
    "nama belakang": "naga",
    "alamat": "bumi",
    "umur": "23",
    "hobi": ["tidur", "hiking"], 
},
{   
    "nama depan": "bon",
    "nama belakang": "mag",
    "alamat": "Munich",
    "umur": "23",
    "hobi": ["kocht", "schwimmt"], 
},
]

BigData.append(
    {
        "nama depan": "jesi",
        "nama belakang": "hoflinger",
        "alamat": "Bonn",
        "umur": "21",
        "hobi": ["fotografiert", "lernt"],
    }
)

print (json.dumps(BigData, indent=4))
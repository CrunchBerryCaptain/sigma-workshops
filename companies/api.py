from flask import Flask, request
import json

# Get all companies
# Get a Company by ID
# Search for a company by name
# Get all companies in country

# Simple authentication stuff (password protected data)

app = Flask(__name__)


def load_companies() -> list[dict]:
    with open('companies.json') as f:
        d = json.load(f)
        return d

    raise ValueError("No file found")


def save_companies(companies: list[dict]) -> None:
    with open('companies.json', 'w') as f:
        json.dump(companies, f)


def filter_companies(companies: list[dict], search_term: str):
    found_companies = []

    for company in companies:
        if search_term in company.get("name"):
            found_companies.append(company)

    return found_companies


def find_next_id(companies: list[dict]) -> int:
    largest_id = 0

    for company in companies:
        id = company.get("id")
        if id > largest_id:
            largest_id = id

    return largest_id + 1


@app.route("/companies", methods=["GET", "POST"])
def get_companies():
    if request.method == "GET":
        companies = load_companies()

        # /companies?[search=chris] - URL query / arguments /args
        search_term = request.args.get("search", None)

        if not search_term:
            return companies, 200

        return filter_companies(companies, search_term), 200
    elif request.method == "POST":
        # Get the data from the post request
        # Check that its all there
        # .  If we don't, return an error
        # If we do, find the next id
        #    Add it to the list of companies

        body = request.json

        if not body.get("name") or not body.get("domain") or not body.get("country") or not body.get("email") or not body.get("stock"):
            return {"error": "Did not include all information"}, 400

        companies = load_companies()

        new_company = {
            "id": find_next_id(companies),
            "name": body.get("name"),
            "domain": body.get("domain"),
            "country": body.get("country"),
            "email": body.get("email"),
            "stock": body.get("stock")
        }

        companies.append(new_company)

        save_companies(companies)

        return {"success": "New company was added"}, 201

    else:
        return {"error": "Not supported"}, 400

# /companies[/13]  - URL param


@app.route("/companies/<int:id>")
def get_company_by_id(id):
    companies = load_companies()

    for company in companies:
        if company.get("id") == id:
            return company, 200

    return {"error": f"Company not found with id {id}"}, 404


@app.route("/companies/<int:id>", methods=["GET", "DELETE"])
def delete_company_by_id(id):
    if request.method == "DELETE":
        # load companies list
        # delete company with matching id
        # save company list
        companies = load_companies()

        for company in companies:
            if company.get("id") == id:
                index = companies.index(company)
                companies.pop(index)
                save_companies(companies)
                return {"success": "Company was deleted"}, 204

        return {"error": "Company not found"}, 404


if __name__ == "__main__":
    app.run(port=8082, debug=True)

# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
The list is named artworks, which makes it easier to understand that each dictionary contains information about one artwork, while the entire list contains all the artworks we have. I think this structure is easier to manage than one big dictionary because each artwork can have different information. For example, if an artwork's artist is unknown, we can simply leave that information out or set it to None without affecting the other artworks.

## 2. Which fields are sometimes missing? What should the app show when they are?
I think the medium and year fields are sometimes missing, and one of the artworks only has a title. When some information about an artwork is missing, we should show "Unknown" to users instead of leaving it blank. This makes it easier for users to understand that the information is not available.
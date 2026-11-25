// Demo records: these make the prototype usable immediately.
const starterItems = [
  { id: 1, type: "Found", name: "Blue water bottle", category: "Accessories", location: "Central library", description: "Blue steel bottle with a black cap.", contact: "lostfound@college.edu" },
  { id: 2, type: "Lost", name: "Scientific calculator", category: "Electronics", location: "Block B, Room 204", description: "Casio calculator with initials M.S. on the back.", contact: "student1@college.edu" },
  { id: 3, type: "Found", name: "Engineering mathematics notebook", category: "Books", location: "Canteen", description: "Brown notebook with a name label inside.", contact: "lostfound@college.edu" },
  { id: 4, type: "Lost", name: "Black headphones", category: "Electronics", location: "Computer lab", description: "Black over-ear headphones in a pouch.", contact: "student2@college.edu" }
];

const STORAGE_KEY = "campusLostFoundItems";
let items = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null") || starterItems;

const results = document.getElementById("results");
const searchInput = document.getElementById("searchInput");

function saveItems() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

function renderItems(list) {
  results.innerHTML = "";
  if (list.length === 0) {
    results.innerHTML = '<p class="empty">No matching reports found. Try different keywords.</p>';
    return;
  }
  list.forEach(item => {
    const card = document.createElement("article");
    card.className = "card";
    // textContent is used for user-provided values to avoid injecting HTML.
    const badge = document.createElement("span");
    badge.className = "badge";
    badge.textContent = item.type;
    const title = document.createElement("h3");
    title.textContent = item.name;
    const category = document.createElement("p");
    category.textContent = "Category: " + item.category;
    const location = document.createElement("p");
    location.textContent = "Location: " + item.location;
    const description = document.createElement("p");
    description.textContent = item.description;
    const contact = document.createElement("p");
    contact.textContent = "Contact: " + item.contact;
    card.append(badge, title, category, location, description, contact);
    results.appendChild(card);
  });
}

function searchItems() {
  const query = searchInput.value.trim().toLowerCase();
  const matches = items.filter(item =>
    [item.type, item.name, item.category, item.location, item.description]
      .some(value => value.toLowerCase().includes(query))
  );
  renderItems(matches);
}

document.getElementById("searchButton").addEventListener("click", searchItems);
document.getElementById("showAllButton").addEventListener("click", () => {
  searchInput.value = "";
  renderItems(items);
});

document.getElementById("itemForm").addEventListener("submit", event => {
  event.preventDefault();
  const newItem = {
    id: Date.now(),
    type: document.getElementById("type").value,
    name: document.getElementById("name").value.trim(),
    category: document.getElementById("category").value,
    location: document.getElementById("location").value.trim(),
    description: document.getElementById("description").value.trim(),
    contact: document.getElementById("contact").value.trim()
  };
  if (!newItem.name || !newItem.location || !newItem.description || !newItem.contact) return;
  items.unshift(newItem);
  saveItems();
  renderItems(items);
  event.target.reset();
  document.getElementById("formMessage").textContent = "Report submitted successfully.";
});

renderItems(items);

# Customer Homepage — Wawa Food Drop

## File
- `src/pages/customer-home.html`

## Page Overview
Customer-facing landing page for browsing restaurants and placing orders.

---

## Navigation Map

### Header (TopAppBar)
| Element | Action | Target Page |
|---------|--------|-------------|
| Logo "Wawa Food Drop" | Click | Home (refresh) |
| Notifications bell | Click | Notifications page |
| Cart icon | Click | Cart page |
| User avatar | Click | Profile page |

### Search Section
| Element | Action | Target |
|---------|--------|--------|
| Search input | Type + Submit | Filter restaurants by name |

### Hero Banner
| Element | Action | Target |
|---------|--------|--------|
| "Explore Menu" button | Click | Restaurant detail (The Harvest Kitchen) |

### Cuisine Filters
| Element | Action | Target |
|---------|--------|--------|
| "View All" link | Click | All cuisines page |
| Fast Food chip | Click | Filtered restaurant list |
| Bakery chip | Click | Filtered restaurant list |
| Pizza chip | Click | Filtered restaurant list |
| Burgers chip | Click | Filtered restaurant list |
| Coffee chip | Click | Filtered restaurant list |
| Dessert chip | Click | Filtered restaurant list |

### Restaurant Grid
| Element | Action | Target |
|---------|--------|--------|
| Filter button (tune icon) | Click | Sort/filter modal |
| Restaurant card | Click | Restaurant detail page |
| Rating stars | Display only | — |
| "Open Now" badge | Display only | — |
| "Closed" badge | Display only | — |

### Mobile FAB
| Element | Action | Target |
|---------|--------|--------|
| Floating basket button | Click | Cart page |

### Bottom Navigation (Mobile)
| Tab | Action | Target |
|-----|--------|--------|
| Explore | Click | Home |
| Orders | Click | Order history |
| Fresh | Click | Fresh deals / promotions |
| Profile | Click | User profile |

---

## Components Identified
- `TopAppBar` — sticky header with logo, icons
- `SearchBar` — full-width search input
- `EditorialBanner` — hero image with gradient overlay
- `CuisineChip` — icon + label filter button
- `RestaurantCard` — image, info, tags, price level
- `StatusBadge` — Open Now / Closed
- `BottomNav` — mobile tab bar
- `FAB` — floating action button

---

## Color Palette (from HTML)
- Primary: `#006d36` (green)
- Secondary: `#ab3500` (orange)
- Background: `#f9f9fc`
- Surface: `#f9f9fc`
- Error: `#ba1a1a`

---

## Notes
- Material Symbols Outlined used for icons
- Tailwind CSS via CDN
- Plus Jakarta Sans font
- Mobile-first responsive design
- Dark mode support via `dark:` classes
/* Lookbook: silver only. Add a figure: drop the image in assets/looks/ and add one entry to SILVER.
   pos: focal point used when the grid crops the square image (CSS object-position).
   items: shop product ids (see shop-data.js) or { name, href }; shown in the full-screen view only. */
/* Silver: jewellery figures, numbered Figure 01, 02 ... */
window.SILVER = [
  { no: 1, image: "assets/looks/silver-01.jpg", pos: "50% 50%", alt: "A wrist in a bead-and-toggle bracelet and a blackletter FC signet ring",
    items: [{ name: "Rings", href: "shop.html?c=ring" }, { name: "Bracelets", href: "shop.html?c=bracelet" }] },
  { no: 2, image: "assets/looks/silver-02.jpg", pos: "50% 40%", alt: "A hand across a face, stacked silver rings and a ball-chain bracelet",
    items: [{ name: "Rings", href: "shop.html?c=ring" }, { name: "Bracelets", href: "shop.html?c=bracelet" }] },
  { no: 3, image: "assets/looks/silver-03.jpg", pos: "50% 45%", alt: "A fist wearing four rings: a cross, the FC signet, a fleur and a dagger",
    items: [{ name: "Rings", href: "shop.html?c=ring" }] },
  { no: 4, image: "assets/looks/silver-04.jpg", pos: "50% 40%", alt: "Two raised fingers with the FC ring and black nails",
    items: [{ name: "Rings", href: "shop.html?c=ring" }, { name: "Bracelets", href: "shop.html?c=bracelet" }] },
  { no: 5, image: "assets/looks/silver-05.jpg", pos: "50% 50%", alt: "A chain wrapped around a hand wearing the FC ring",
    items: [{ name: "Rings", href: "shop.html?c=ring" }, { name: "Necklaces", href: "shop.html?c=necklace" }] },
  { no: 6, image: "assets/looks/silver-06.jpg", pos: "50% 55%", alt: "Clasped hands with engraved silver bands",
    items: [{ name: "Rings", href: "shop.html?c=ring" }] },
  { no: 7, image: "assets/looks/silver-07.jpg", pos: "50% 50%", alt: "Ringed hands holding a phone, the FC Crewneck behind",
    items: ["fc-crewneck", { name: "Rings", href: "shop.html?c=ring" }, { name: "Bracelets", href: "shop.html?c=bracelet" }] },
  { no: 8, image: "assets/looks/silver-08.jpg", pos: "50% 40%", alt: "A hand at the collar of the FC Crewneck, a toggle necklace and rings",
    items: ["fc-crewneck", { name: "Necklaces", href: "shop.html?c=necklace" }, { name: "Rings", href: "shop.html?c=ring" }] },
];

/* Full-bleed plates: the first opens the lookbook, the last closes it. */
window.BLEED = {
  first: { key: "prayer", title: "Prayer", kicker: "Silver", image: "assets/looks/bleed-prayer.jpg", ratio: "2688 / 1520",
    alt: "Hands pressed together in prayer, stacked with blackletter rings, a toggle chain and bracelets",
    items: [{ name: "Rings", href: "shop.html?c=ring" }, { name: "Bracelets", href: "shop.html?c=bracelet" }, { name: "Necklaces", href: "shop.html?c=necklace" }] },
  last: { key: "congregation", title: "Congregation", kicker: "Before the Altar", image: "assets/looks/bleed-congregation.jpg", ratio: "2688 / 1520",
    alt: "Four figures seen from behind, standing before the glowing Dataism cross in the FAKE CHURCH garments",
    items: ["stacked-denim", "boxy-tee", "ribbed-beanie", "sweat-shorts", "ma1-bomber", { name: "The Altar", href: "index.html#altar" }] },
};

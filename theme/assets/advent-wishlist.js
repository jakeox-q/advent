/* Advent: simple wishlist heart on product cards. Saves product handles in this browser (localStorage key "advent-wishlist").
   Placeholder until a wishlist app is chosen: remove the render line in snippets/advent-card-badges.liquid to take it out. */
(function () {
  if (window.customElements && customElements.get('advent-wishlist')) return;
  var KEY = 'advent-wishlist';
  function read() { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
  function write(list) { try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) {} }
  class AdventWishlist extends HTMLElement {
    connectedCallback() {
      this.btn = this.querySelector('button');
      if (!this.btn) return;
      this.handle = this.dataset.handle;
      this.render();
      this.btn.addEventListener('click', (e) => {
        e.preventDefault(); e.stopPropagation();
        var list = read(); var i = list.indexOf(this.handle);
        if (i > -1) list.splice(i, 1); else list.push(this.handle);
        write(list);
        document.querySelectorAll('advent-wishlist[data-handle="' + this.handle + '"]').forEach(function (el) { el.render && el.render(); });
      });
    }
    render() {
      var on = read().indexOf(this.handle) > -1;
      this.btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      this.btn.setAttribute('aria-label', on ? this.btn.dataset.labelRemove : this.btn.dataset.labelAdd);
      this.classList.toggle('is-saved', on);
    }
  }
  customElements.define('advent-wishlist', AdventWishlist);
})();

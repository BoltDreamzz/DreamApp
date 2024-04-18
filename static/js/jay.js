<script>
    <script>
      document.addEventListener('DOMContentLoaded', function () {
        var addButton = document.querySelectorAll('.addButton');
        var removeButton = document.querySelectorAll('.removeButton');
        var wishlistToast = new bootstrap.Toast(document.getElementById('wishlistToast'));
        var removedFromWishlistToast = new bootstrap.Toast(document.getElementById('removedFromWishlistToast'));

        addButton.forEach(function (btn) {
          btn.addEventListener('click', function (event) {
            event.preventDefault();
            // Logic to add product to wishlist
            var productId = this.getAttribute('data-product-id');
            // Assuming product is added successfully, show the toast
            wishlistToast.show();
          });
        });

        removeButton.forEach(function (btn) {
          btn.addEventListener('click', function (event) {
            event.preventDefault();
            // Logic to remove product from wishlist
            var productId = this.getAttribute('data-product-id');
            // Assuming product is removed successfully, show the toast
            removedFromWishlistToast.show();
          });
        });
      });
</script>

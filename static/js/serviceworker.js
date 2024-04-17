//if ('serviceWorker' in navigator) {
//        navigator.serviceWorker.register('static/js/serviceworker.js')
//            .then((registration) => {
//                console.log('Service Worker registered with scope:', registration.scope);
//            })
//            .catch((error) => {
//                console.error('Service Worker registration failed:', error);
//            });
//    }
//
//
//var staticCacheName = 'djangopwa-v1';
//
//self.addEventListener('install', function(event) {
//event.waitUntil(
//	caches.open(staticCacheName).then(function(cache) {
//	return cache.addAll([
//		'',
//	]);
//	})
//);
//});
//
//self.addEventListener('fetch', function(event) {
//var requestUrl = new URL(event.request.url);
//	if (requestUrl.origin === location.origin) {
//	if ((requestUrl.pathname === '/')) {
//		event.respondWith(caches.match(''));
//		return;
//	}
//	}
//	event.respondWith(
//	caches.match(event.request).then(function(response) {
//		return response || fetch(event.request);
//	})
//	);
//});
//
//
//
////// myapp/static/myapp/service-worker.js
////
////self.addEventListener('install', (event) => {
////    event.waitUntil(
////        caches.open('my-cache').then((cache) => {
////            return cache.addAll([
////                '/',
//////                '/static/shop_media/styles.css',
//////                '/static/myapp/main.js'
////                // Include other assets you want to cache
////            ]);
////        })
////    );
////});
////
////self.addEventListener('fetch', (event) => {
////    event.respondWith(
////        caches.match(event.request).then((response) => {
////            return response || fetch(event.request);
////        })
////    );
////});

(function(){
	angular.module('kabbageService', [])
	.config(function($locationProvider){
		$locationProvider.html5Mode({
			enabled: true,
			requireBase: false
			});
	})
	.factory('WikipediaService', ['$http', '$location', function($http, $location){
		var getWikipediaItems = function (){
			var queryParams = $location.search();
			var searchTerm = queryParams['search'];
			return $http.get('/api/search/?search=' + searchTerm + '&service=wikipedia');
		};
		return{
			'getWikipediaItems': getWikipediaItems
		}
	}])
	.factory('TwitterService', ['$http', '$location', function($http, $location){
		var getTwitterItems = function (){
			var queryParams = $location.search();
			var searchTerm = queryParams['search'];
			return $http.get('/api/search/?search=' + searchTerm + '&service=twitter');
		};
		return{
			'getTwitterItems': getTwitterItems
		}
	}]);
})();

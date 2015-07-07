(function(){
	angular.module('kabbageService', [])
	.config(function($locationProvider){
		$locationProvider.html5Mode({
			enabled: true,
			requireBase: false
			});
	})
	.factory('WikipediaService', ['$http', function($http){
		var getWikipediaItems = function (searchTerm){
			return $http.get('/api/search/?search=' + searchTerm + '&service=wikipedia');
		};
		return{
			'getWikipediaItems': getWikipediaItems
		}
	}])
	.factory('TwitterService', ['$http', function($http){
		var getTwitterItems = function (searchTerm){
			return $http.get('/api/search/?search=' + searchTerm + '&service=twitter');
		};
		return{
			'getTwitterItems': getTwitterItems
		}
	}]);
})();

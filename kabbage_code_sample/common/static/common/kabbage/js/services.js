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
			searchTerm['search'] = searchTerm['search'].split(' ').join('%20');
			if(searchTerm['latitude']){
				return $http.get('/api/search/?search=' + searchTerm['search'] + '&service=wikipedia&latitude=' + searchTerm['latitude'] + '&longitude=' + searchTerm['longitude']);
			}else{
				return $http.get('/api/search/?search=' + searchTerm['search'] + '&service=wikipedia');
			}
		};
		return{
			'getWikipediaItems': getWikipediaItems
		}
	}])
	.factory('TwitterService', ['$http', function($http){
		var getTwitterItems = function (searchTerm){
			searchTerm['search'] = searchTerm['search'].split(' ').join('%20');
			if(searchTerm['latitude']){
				return $http.get('/api/search/?search=' + searchTerm['search'] + '&service=twitter&latitude=' + searchTerm['latitude'] + '&longitude=' + searchTerm['longitude']);
			}else{
				return $http.get('/api/search/?search=' + searchTerm['search'] + '&service=twitter');
			}
		};
		return{
			'getTwitterItems': getTwitterItems
		}
	}]);
})();

angular.module('blstApp').factory('MainService', function ($resource) {
    return {
        bucketlists: $resource('/api/bucketlists/', {}, {
            getBucketlists: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        })
    };
});

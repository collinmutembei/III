angular.module('blstApp').factory('MainService', function ($resource) {
    return {
        bucketlists: $resource('/api/bucketlists/', {}, {
            getBucketlists: {
                method: 'GET',
                isArray: true
            },
            addBucketlist: {
                method: 'POST',
            }
        }, {
            stripTrailingSlashes: false
        }),
        single_bucketlist: $resource('/api/bucketlists/:id/', {id:'@id'}, {
            getBucketlist: {
                method: 'GET',
                isArray: false
            },
            updateBucketlist: {
                method: 'PUT'
            }
        })
    };
});

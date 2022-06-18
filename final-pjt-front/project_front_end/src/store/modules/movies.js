import axios from 'axios'
import router from '@/router'
import drf from '@/api/drf'

export default {
    state: {
        currentUser: {},
        movies: [],
        movie: [],
        genre: [],
        similar: [],
        search: [],
        similardetail: [],
        like: {},
    },
    getters: {
        movies: state => state.movies,
        movie: state => state.movie, 
        genre: state => state.genre,
        similar: state => state.similar,
        search: state => state.search,
        similardetail: state => state.similardetail,
        like: state => state.like,
    },
    
    mutations: {
        SET_MOVIES: (state,movies) => state.movies = movies,
        SET_MOVIE: (state, movie) => state.movie = movie,
        SET_GENRE: (state,genre) => state.genre = genre,
        SET_SIMILAR: (state,similar) => state.similar = similar,
        SET_SEARCH: (state,search) => state.search = search,
        SET_SIMILARDETAIL: (state,similardetail) => state.similardetail = similardetail,
        SET_LIKE: (state,like) => state.like = like
    },
  
    actions: {

        // 영화 전체 목록 state 저장
        fetchMovies({ commit, getters }){
            axios({
                url: drf.movies.movies(),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_MOVIES', res.data)) 
            .catch(err => console.error(err.response))
        },
        // 개별 영화 state
        fetchMovie({commit , getters},movieId){
            axios({
                url: drf.movies.movie(movieId),
                method: 'get',
                headers: getters.authHeader, 
            })
            .then(res => commit('SET_MOVIE', res.data))
            .catch(err => {
                console.error(err.response)
                if (err.response.status === 404){
                    router.push({ name: 'NotFound404' })
                }
            })
        },
        fetchSimilarDetail({commit , getters},movieId){
            axios({
                url: drf.movies.similar_detail(movieId),
                method: 'get',
                headers: getters.authHeader, 
            })
            .then(res => commit('SET_SIMILARDETAIL', res.data))
            .catch(err => {
                console.error(err.response)
                if (err.response.status === 404){
                    router.push({ name: 'NotFound404' })
                }
            })
        },
        // 장르별 영화 목록 state 저장
        fetchGenre({commit, getters},genreId){
            axios({
                url: drf.movies.genres(genreId),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_GENRE', res.data))
            .catch(err => console.error(err.response))
        },
        fetchSimilar({commit, getters},movieId){
            axios({
                url: drf.movies.similar(movieId),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_SIMILAR', res.data))
            .catch(err => console.error(err.response))
        },
        
        // 개별 영화 좋아요 
        likeMovie({commit, getters},movieId){
            axios({
                url: drf.movies.likeMovie(movieId),
                method: 'post',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_LIKE', res.data))
            .catch(err => console.error(err.response))
        },
        searchMovie({commit,getters},movieTitle){
            axios({
                url : drf.movies.search(movieTitle),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_SEARCH', res.data))
            .catch(err => console.error(err.response))
        },
      },
  }
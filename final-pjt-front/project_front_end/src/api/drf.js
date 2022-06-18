const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,

    // 만약 아래 코드에서 버그 발생 시 백엔드 세팅에서 인증 방식 변경 (디버깅 용도로 모두 허용 중)
    // 'DEFAULT_PERMISSION_CLASSES' -> 'rest_framework.permissions.IsAuthenticated'
    // 아래 코드는 토큰을 발급받은 인증된 유저인지 확인하는 url을 연결합니다.
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',

    follow: userPk => HOST + ACCOUNTS + 'profile/' + `${userPk}/` + 'follow/' // follow

  },
  community: {
    reviews: () => HOST + COMMUNITY,   // 전체 리뷰 목록
    review: reviewPk => HOST + COMMUNITY + `${reviewPk}/`,   // 리뷰글 디테일
    createReview: () => HOST + COMMUNITY + 'create/', // 리뷰 생성
    likeReview: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + 'like/',  // 리뷰 좋아요
    comments: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + COMMENTS, // 댓글 전체 목록
    comment: (reviewPk, commentPk) => HOST + COMMUNITY + `${reviewPk}/` + COMMENTS + `${commentPk}/`, // 단일 댓글
  },
  movies: {
    movies: () => HOST + MOVIES,
    // 문제 발생시 백엔드 movies/ 관련 코드 및 아래 코드 movie_pk로 수정
    movie: movieId => HOST + MOVIES + 'detail/' + `${movieId}/`,  // 영화 세부 정보
    genres: genreId => HOST + MOVIES + 'genre/' + `${genreId}`,  // 장르 정보들, 세부명들의 필요성은 추후 재고
    similar: movieId => HOST + MOVIES + 'similar/' + `${movieId}/`,
    similar_detail: movieId => HOST + MOVIES + 'similar/' + 'detail/' + `${movieId}/`, 
    likeMovie: movieId => HOST + MOVIES + `${movieId}/` + 'like/', // 영화 좋아요
    search: movieTitle => HOST + MOVIES + 'search/' + `${movieTitle}/`, // 영화 서치
},

}
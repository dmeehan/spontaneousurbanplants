var gulp = require('gulp');

var bower = require('gulp-bower');

gulp.task('default', function() {
  // place code for your default task here
});

gulp.task('bower', function() {
  bower()
    .pipe(gulp.dest('lib/'))
});


var gulp = require('gulp');


// handle dependencies
gulp.task('dependencies', function() {
	gulp.src('node_modules/normalize.css/normalize.css')
		.pipe(gulp.dest('export'));
});


// process css
var stylus = require('gulp-stylus');

gulp.task('stylus', function() {
	gulp.src('source/*.styl')
		.pipe(stylus())
		.pipe(gulp.dest('export'));
});


// process images
gulp.task('image', function() {
	gulp.src('source/*png')
		.pipe(gulp.dest('export'));
});


// what to watch for
gulp.task('watch', function() {
    gulp.watch('source/*.styl', ['stylus']);
});


// the default task
gulp.task('default', function() {
	gulp.start([
		'dependencies',
        'stylus',
		'image',
		'watch'
	]);
});

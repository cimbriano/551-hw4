#!/usr/bin/perl

use strict;
use CGI qw(:standard escapeHTML);

my $cmd = "echo ".param("cookie");

print header, start_html("web-ls");



print "<h2>";
print "$cmd";
print "</h2>";
print "<pre>\n";

$cmd=`$cmd`;
print "$cmd\n";

print "</pre>";
print end_html;


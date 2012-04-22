#!/usr/bin/perl

use strict;
use HTML::Entities ();
use CGI qw(:standard escapeHTML);
print header, start_html("web-ls");

my $command = "ls -la /var/www/";
$command = $command.sanitize(param("dir"));

print "<h2>";
print "$command";
print "</h2>";
print "<pre>\n";

$command=`$command`;
print "$command\n";

print "</pre>";
print end_html;

sub sanitize {
    my $html = HTML::Entities::decode(shift);

    $html =~ s/[;|&&|\|\|].*//g;
    $html =~ s/[^\w \-,]//g; 

    return $html;
}

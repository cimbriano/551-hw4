#!/usr/bin/perl

use strict;
use HTML::Entities ();
use CGI qw(:standard escapeHTML);
print header, start_html("web-ls");

my $command = "ls -la /var/www/";

# Call santize on the user input
$command = $command.sanitize(param("dir"));

print "<h2>";
print "$command";
print "</h2>";
print "<pre>\n";

$command=`$command`;
print "$command\n";

print "</pre>";
print end_html;




# Sanitizes a user-inputted string
sub sanitize {
    
    my $html = HTML::Entities::decode(shift);

    # Substitue with nothing (remove) all characters 
    #   which are not word characters, spaces, dashes or commas
    $html =~ s/[^\w \-,]//g; 

    # Return the sanitized string
    return $html;
}

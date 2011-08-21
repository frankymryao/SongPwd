#! /usr/bin/perl

$ENV{'WORKPATH'} = "/Users/frank/SongPwd";

system "rm $ENV{'WORKPATH'}/breakData";
system "touch $ENV{'WORKPATH'}/breakData";

my @pwd_type = qw/ number alphabet mix/;
my $cmd_tail;
my $mask;
my %short_times = (
        "number"=> 7,
        "alphabet" => 4,
        "mix" => 4,
);
my %long_times = (
        "number"=> 8,
        "alphabet" => 5,
        "mix" => 5,
);

foreach my $type (@pwd_type) {
    for(my $i=0;$i<5;$i++) {
        $cmd = $ENV{'WORKPATH'}.'/force.py';
        $cmd_tail = "$type"." $short_times{$type}";
        $cmd .= " ".$cmd_tail.$mask;
        print $cmd_tail." is RUNNING...\n";
        system $cmd."\n";
        print $cmd_tail." is DONE!\n";
    }
        $cmd = $ENV{'WORKPATH'}.'/force.py';
        $cmd .= " $type"." $long_times{$type}";
        system $cmd."\n";
}
                                                                    



require 'digest'
s = Random.new(0)
SEED = '0'
pass = 6.times.map { ('a'..'z').to_a[s.rand(('a'..'z').to_a.size)]}.join
puts pass
#puts Digest::MD5.hexdigest(SEED+pass+SEED)

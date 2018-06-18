# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |v|
      v.memory = 1536
      # v.cpus = 2
  end

  # force (virtualbox) VMs to update time from the host a bit more aggressively otherwise clock drifts
  # quite a lot and ntp does nothing in a VM. See '9.14.3. Tuning the Guest Additions time synchronization parameters'
  # on this: https://www.virtualbox.org/manual/ch09.html and also
  # http://jeremykendall.net/2014/10/06/forcing-an-ntp-update/ :
  config.vm.provider :virtualbox do |v|
      v.customize ["guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000]
  end

end

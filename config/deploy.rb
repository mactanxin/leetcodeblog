# config valid only for current version of Capistrano
lock '3.4.0'
require 'capistrano-rbenv'
load 'deploy/assets'
ssh_options[:port] = 22022

set :copy_local_tar, "/usr/bin/tar" if RUBY_PLATFORM.match(/darwin/)
set :application, 'leetcodeblog'
set :repository, "."
set :scm, :none
set :deploy_via, :copy
set :repo_url, 'git@example.com:me/my_repo.git'

SERVER_TEST = "10.103.13.81"


set(:server_type) {
  puts "== 测试服务器是：  81 "
  puts "== 部署mpcms "
  Capistrano::CLI.ui.ask("== which server do you want to deploy to? (81)? ")
}
case server_type.chomp
  when '81'
    server = SERVER_TEST
    password = 'yXuGXzEBdd3e'
end
puts "== password for #{server} is: #{password}"

role :web, server
role :app, server
role :db,  server, :primary => true
role :db,  server

set :deploy_to, "/opt/app/python/leetcodeblog"
cms_shared_path = "/opt/app/python/leetcodeblog/shared"
deploy_to_path = "/opt/app/python/leetcodeblog"
default_run_options[:pty] = true

# change to your username
set :user, "root"

namespace :deploy do
  task :start do
   # run 'uwsgi -x django.xml'
    puts "start"
  end
  task :stop do
    puts "stop"
  end
  task :restart, :roles => :app, :except => { :no_release => true } do
    run "touch /opt/app/python/mpcms/current"
  end

   namespace :assets do
    task :precompile do
    end
  end
end

desc "Copy setting.py to release_path"
task :cp_setting_py do
  puts "=== executing my customized command: "
  run "cp -r #{shared_path}/settings.py #{release_path}/mpcms/"
  run "cp -r #{shared_path}/settings_for_fetch.py #{release_path}/scripts/"
  run "chmod -R 777 #{shared_path}"
  puts "=== done (executing my customized command)"
end

before "deploy:assets:precompile", :cp_setting_py

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, '/var/www/my_app_name'

# Default value for :scm is :git
# set :scm, :git

# Default value for :format is :pretty
# set :format, :pretty

# Default value for :log_level is :debug
# set :log_level, :debug

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# set :linked_files, fetch(:linked_files, []).push('config/database.yml', 'config/secrets.yml')

# Default value for linked_dirs is []
# set :linked_dirs, fetch(:linked_dirs, []).push('log', 'tmp/pids', 'tmp/cache', 'tmp/sockets', 'vendor/bundle', 'public/system')

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for keep_releases is 5
# set :keep_releases, 5


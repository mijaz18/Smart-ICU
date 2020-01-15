%% House Keeping
clear all
clc
%%
load data_expiry_percent_mortality_mimic_eth.mat 
thre = 0:100;
diff = zeros(1,length(thre));
exp_true = sum(exp);
for y = 1:length(thre)
    count = 0;
    for x = 1:length(p_m)
        if (p_m(x) > thre(y))
            count = count + 1;
        end
    end
    exp_calc = count;
    diff(y) = abs(exp_true - exp_calc);
end
%plot(diff)
%% Comparison checker against subject ids
exp = logical(exp);
thre = 0:100;
for thresh = 1:length(thre);
    death_chk = p_m > thre(thresh);
    comp = exp ~= death_chk;
    diff_index(thresh) = sum(comp);
end
%% plot results

plot(diff_index)
[val ind] = min(diff_index);
sum (p_m > ind) - exp_true

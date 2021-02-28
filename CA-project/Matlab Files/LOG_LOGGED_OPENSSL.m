marker_size = 14;
line_width = 2;
font_size = 14;
color = 'black'

data = readmatrix('LOGGED_OPENSSL.csv');

plot = 1

%timestamp = data(:,1);
timestamp_seconds = data(:,2);
%algorithm = data(:,3);
avg_keygen_time = data(:,4) / 10;
avg_csr_time = data(:,5) / 10;
avg_cert_time = data(:,6) / 10;
avg_verifying_time = data(:,7) / 10;
combined_data = [avg_keygen_time avg_csr_time avg_cert_time avg_verifying_time];

maxLim = 0
if plot == 1
    y = avg_keygen_time;
    b = bar(y, color);
    maxLim = max(y) * 3;
elseif plot == 2
    y = avg_csr_time;
    b = bar(y, color) 
    maxLim = max(y) * 1.3;
elseif plot == 3
    y = avg_cert_time;
    b = bar(y, color);
    maxLim = max(y) * 1.3;
elseif plot == 4
    y = avg_verifying_time;
    b = bar(y, color);
    maxLim = max(y) * 1.1;
end

set(gca, 'YScale', 'log');
ylim([0 maxLim]);

%xlabel('Algorithm', 'FontSize', font_size);
xticklabels({'RSA 2048', 'RSA 3072', 'RSA 4096', 'Dilithium 2', 'Dilithium 3', 'Dilithium 4', 'Falcon 512', 'Falcon 1024', 'RSA 3072 - Dilithium 2', 'RSA 3072 - Dilithium 3', 'RSA 3072 - Falcon 512', 'P256 - Dilithium 2', 'P256 - Dilithium 3', 'P384 - Dilithium 4', 'P256 - Falcon 512'});
xtickangle(45);
ylabel('Time Cost (ms)', 'FontSize', font_size);
set(gca,'FontSize', font_size);
set(gca, 'YGrid', 'on', 'XGrid', 'off');


if plot == 1
    set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
elseif plot == 2
    %set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
elseif plot == 3
    %set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
elseif plot == 4
    set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
end

h = text(1:length(y'),y'*1.01,num2str(round(y*100)/100),'vert','middle','horiz','left', 'FontSize', font_size); 
set(h,'Rotation', 90);

width = 600;
height = 800
set(gcf,'position',[100,100,width,height])

axis square;
%legend('Key generation', 'CSR generation', 'Certificate generation', 'Certificate verification', 'FontSize', font_size);


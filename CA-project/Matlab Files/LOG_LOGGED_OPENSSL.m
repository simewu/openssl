marker_size = 14;
line_width = 2;
font_size = 14;
color_classical = '#2CBAD4';
color_postquantum = '#7900EF';
color_hybrid = '#F00074';

data = readmatrix('LOGGED_OPENSSL.csv');

plot = 3;

%timestamp = data(:,1);
timestamp_seconds = data(:,2);
%algorithm = data(:,3);
avg_keygen_time = data(:,4) / 10;
avg_csr_time = data(:,5) / 10;
avg_cert_time = data(:,6) / 10;
avg_verifying_time = data(:,7) / 10;
combined_data = [avg_keygen_time avg_csr_time avg_cert_time avg_verifying_time];

maxLim = 0;
if plot == 1
    y = avg_keygen_time;
    maxLim = max(y) * 3;
elseif plot == 2
    y = avg_csr_time;
    maxLim = max(y) * 1.3;
elseif plot == 3
    y = avg_cert_time;
    maxLim = max(y) * 1.3;
elseif plot == 4
    y = avg_verifying_time;
    maxLim = max(y) * 1.1;
end

b = bar(y, 'Visible', 'off', 'HandleVisibility', 'off'); % Skeleton
y = avg_keygen_time;
clset = 0;
pqset = 0;
hyset = 0;
hold on;
for i=1:length(y)
    b_ = bar(i, y(i));
    if i <= 3 % Classical
        set(b_, 'FaceColor', color_classical);
        if clset ~= 0
            set(b_, 'HandleVisibility', 'off');
        end
        clset = 1;
    elseif i <= 8 % Post quantum
        set(b_, 'FaceColor', color_postquantum);
        if pqset ~= 0
            set(b_, 'HandleVisibility', 'off');
        end
        pqset = 1;
    else % Hybrid
        set(b_, 'FaceColor', color_hybrid);
        if hyset ~= 0
            set(b_, 'HandleVisibility', 'off');
        end
        hyset = 1;
    end
end
hold off;

set(gca, 'YScale', 'log');
%ylim([0 maxLim]);

%xlabel('Algorithm', 'FontSize', font_size);
xticklabels({'RSA 2048', 'RSA 3072', 'RSA 4096', 'Dilithium 2', 'Dilithium 3', 'Dilithium 4', 'Falcon 512', 'Falcon 1024', 'RSA 3072 - Dilithium 2', 'RSA 3072 - Dilithium 3', 'RSA 3072 - Falcon 512', 'P256 - Dilithium 2', 'P256 - Dilithium 3', 'P384 - Dilithium 4', 'P256 - Falcon 512'});
xtickangle(45);
%ylabel('Time Cost (ms)', 'FontSize', font_size);
if plot == 1
    ylabel('Key Generation Time Cost (ms)', 'FontSize', font_size);
elseif plot == 2
    ylabel('CSR Generation Time Cost (ms)', 'FontSize', font_size);
elseif plot == 3
    ylabel('Certificate Generation Time Cost (ms)', 'FontSize', font_size);
elseif plot == 4
    ylabel('Verifying Time Cost (ms)', 'FontSize', font_size);
end
set(gca,'FontSize', font_size);
set(gca, 'YGrid', 'on', 'XGrid', 'off');

legend('Classical', 'Post-quantum', 'Hybrid')


if plot == 1
    set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
elseif plot == 2
    set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
elseif plot == 3
    set(gca,'YTickLabel',num2str(get(gca,'YTick').'));
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


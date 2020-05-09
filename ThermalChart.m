Z=[ 54.34 ,  55.46 ,  56.88 ,  57.36 ; 55.46 ,  56.88 ,  57.36 ,  60.3 ; 55.46 ,  57.36 ,  59.57 ,  62.87 ; 55.46 ,  57.36 ,  60.3 ,  62.87 ; 55.46 ,  57.36 ,  60.3 ,  62.87 ; 55.46 ,  57.36 ,  62.87 ,  62.87 ]
b = bar3(Z);
zlim([45 65])
caxis([45 65])
c=colorbar;
c.Label.String = '[°C]';
colormap('jet');
xticklabels({'1.0E-02','1.0E-05','1.0E-07','1.0E-09'});
xtickangle(-45);
ylabel('Year')
set(get(gca,'ylabel'),'rotation',-40)
xlabel('PoF Target');
set(get(gca,'xlabel'),'rotation',35)
ax = gca;
ax.FontSize = 21;

yticklabels({'0','1','2','3','4','5'});
for k = 1:length(b)
    zdata = b(k).ZData;
    b(k).CData = zdata;
    b(k).FaceColor = 'interp';
end
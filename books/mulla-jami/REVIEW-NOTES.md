# Review notes — Mulla Jami translation

> **Page references here are book pages** (the numbers printed in the Şifa 2015
> edition, e.g. book p.٣٠٥), which never change. Each release also includes
> `Mulla-Jami_Review-Notes.md`, the same list with the PDF page of that
> release's `Mulla-Jami_Manuscript.pdf` added to every reference.

## Status: re-read at high resolution

Pages 24–92 have been **re-read from high-DPI renders** (`tools/hires_page.py`
renders each page at 500–700 dpi in bands so the ḥawāshī are fully legible). An
earlier low-resolution pass had *reconstructed* some faint-looking footnote text;
those reconstructions have been replaced with what is actually printed. No
`# REVIEW:` reconstruction flags remain in the page files. From here on, every
page is read at high DPI from the start (mandated in `TRANSLATION-GUIDE.md`).

Notable corrections from the re-read (a sample): a whole **missing footnote**
restored on book p.٤٣; a footnote that was an entirely wrong gloss replaced with its
real al-Raḍī citation on book p.٦١; several meaning-reversing misreadings fixed
(e.g. `بمعنى` → `لا بمعنى`); and on **book p.٢٣ footnote 7** the disputed word is
**«علي»** (ʿAlī), not «الأصحاب» as first guessed — now corrected.

## ⚠ Source gap — printed page ٢٨ is missing

PDF page 29 is a **blank leaf** in the scan, so **printed page ٢٨ was never
scanned**. The build skips it (٢٧ → ٢٩). Please send that page to fill the gap.

## Batch 3 (book pp.٩٢–١٤١, read at high DPI)

Translated directly from high-DPI renders — no reconstructions. A few tiny
print-oddities transcribed faithfully, worth a glance:
- **book p.٩٩ matn**: the base-text verb has an ambiguous ص/ض glyph; read as `صُرِفَ`
  (ṣurifa), confirmed by its footnotes.
- **book p.١٢٦ footnote 6**: print shows `المبتدأ واسلخبر`; rendered the intended
  `المبتدأ والخبر`.
- **book p.١٣٩ footnote 5**: `الثبوت التي خبرها` is grammatically irregular in the
  print; transcribed as-is.

New TOC chapters added: al-Waṣf, al-ʿUjma, al-Jamʿ, al-Alif wa-l-Nūn, Wazn
al-Fiʿl, al-Tarkīb, al-Maʿrifa, Kasr al-Mamnūʿ, al-Marfūʿāt, al-Fāʿil,
Taqdīm/Taʾkhīr al-Fāʿil, Ḥadhf al-Fiʿl, al-Tanāzuʿ.

## Batch 4 (book pp.١٤٢–١٩١, read at high DPI)

Printed ١٤٢–١٩١. All marker/footnote counts balance; footnotes running over a
page break are carried as unnumbered continuation notes (book p.١٥٤, 160, 164,
176, 178). Each item below is clearly printed but looks like a misprint or is
unusually terse; the Arabic is transcribed as printed (most carry a
`# REVIEW:` comment in the page file):

- **book p.١٤٢ fn ٤**: «فإن أعلمت» beside «فإن أعملت» on the line above; translated as أعملت.
- **book p.١٤٣ fn ١**: «ضربت وحبست زيداً منطلقاً» — perhaps «حسبت».
- **book p.١٤٩ fn ٥**: «لأنَّ المتكلم…» — the argument suggests «لا أنَّ».
- **book p.١٥٠ fn ٥**: «عل تقدير» for «على تقدير».
- **book p.١٥٣–155 fn ٦**: «أظهرَ كلَّ / الاختفاءِ» across the page break — legible, sense unclear.
- **book p.١٥٥ matn**: «فمعنى الابتداءِ عاملٌ في المبتدأِ. والخبرُ رافعٌ لهما» — translated as one statement; please confirm.
- **book p.١٥٩ fn ٤**: «وإن كان عالماً بها يصحّ الإخبار» — the sense calls for «لا يصحّ».
- **book p.١٦٠ fn ٤**: «معنى كان زيد أخوك هو» — «كان» may be a misprint.
- **book p.١٦١ matn**: «لا بسعر غيرهما» — elliptical; English supplies the gap in brackets.
- **book p.١٦٢ fn ٢**: «والتقوى يقوي الإفراد» — terse; "[the absence of]" is an interpretation.
- **book p.١٦٤ fn ٣**: «غلام زيد راكب» — the argument suggests «غلامُ مَن».
- **book p.١٦٧ fn ٧**: «في هذه الإشكال» and «سهولة حال العاقل» as printed.
- **book p.١٧٢ fn ٦**: «من الصدر صورةً» — perhaps «المصدر».
- **book p.١٧٣ fn ١**: «بالفعل» — "the verb" or "actually"?
- **book p.١٧٣ fn ٥**: «كما يخفى» for the usual «كما لا يخفى» (confirmed at 700 dpi).
- **book p.١٧٤ fn ٨**: «مُصْحَفِها» read as «مُصَحَّفها» (graphic variant).
- **book p.١٨٠ fn ٣**: «فقد يعد» — read as «فقد بَعُدَ».
- **book p.١٨٥ fn ٤**: «تحدد الأمثال» — translated as تجدد.
- **book p.١٨٨ fn ٧**: «لا نفي العبارة» — translated as «لا تفي».
- **book p.١٨٩ fn ٣**: «فأما قراءة…» — translated as «فإما»; fn ٧ last sentence obscure, rendered literally.
- **book p.١٩٠ matn**: a closing » after «فداءً» with no opening guillemet.
- **book p.١٩١ matn**: «صوَّت توصيتاً» for «تصويتاً»; **fn ٦**: «من المصادرة», probably «من المصادر».

## Diacritics removed (2026-11-01)

At your request every diacritic (ḥarakāt, shadda, sukūn, tanwīn, dagger alif) was
removed from all pages, including those printed in the book, and none is added
from book p.١٩٢ onward. `tools/check_page.py` rejects any page that contains one.

## Batch 5 (book pp.١٩٢–٢٤١, read at high DPI, no diacritics)

Printed ١٩٢–٢٤١. All marker/footnote counts balance. Clear in print but odd or
likely misprinted (transcribed as printed, `# REVIEW:` in the file):

- **book p.١٩٣**: fn ٣ «ضرب زيد ضربته» (dual expected); fn ٧ «يمثله» for «يمتثله».
- **book p.١٩٤ matn**: «يتعدى اللام» for «باللام».
- **book p.١٩٥ fn ٨**: «إما جائزا، وإما واجب، وإما ممتنع» (mixed case).
- **book p.١٩٦ fn ٥**: «ولا ينقلب شيء» (checked at 800 dpi); English tentative.
- **book p.١٩٧ fn ٣**: «تفريع» for «تفريغ».
- **book p.١٩٨ matn**, **book p.٢٠٤ heading**: «المنادي» with yāʾ.
- **book p.١٩٩ fn ٥**: «اسم الفاعل», where the argument concerns «اسم الفعل».
- **book p.٢٠٢**: fn ٦ «مبنئ» for «منبئ»; fn ٧ «ليخصر» for «ليحضر».
- **book p.٢٠٩**: matn «والكسرة مناسبة للتخفيف» (perhaps «والكثرة»); fn ١ «التوابع المضاف».
- **book p.٢١٠ fn ٧**: «والنصف» for «والنصب».
- **book p.٢١١**: «للكملة»/«بكملة» for «للكلمة»/«بكلمة»; matn «أشذ» vs fn ٤ «أشد».
- **book p.٢١٢ fn ٤**: «إن «إن زيدا قائم»» — intended example unclear.
- **book p.٢١٤ matn**: «فقوله» for «بقوله».
- **book p.٢١٥**: fn ٤ «فاعلمها» for «فاعلهما», verse «أذمى» (known reading «إذ مي»); fn ٧ «خذف» for «حذف».
- **book p.٢١٦**: matn «ترخيم المنادى بالمقايسة» — sense requires «غير المنادى»; fn ٩ poetry inside ﴿﴾.
- **book p.٢١٩**: fn ١ «اثنا عشرة»; fn ٢ «ورحمت» for «ورخمت».
- **book p.٢٢١**: matn «ليرد»; fn ٤ «إلا المعروف» vs matn «إلا المعرفة».
- **book p.٢٢٣ fn ٦**: «تغييرهن». **book p.٢٢٤ matn**: «فلا تخلي أيضا» translated by sense.
- **book p.٢٢٩ fn ٤**: «علة جملة» (lemma «على جملة»); «زيد عمر وقائم».
- **book p.٢٣١ matn**: «عل تقدير». **book p.٢٣٢ fn ٧**: «كـ«أل» للعرض»; «في أن امرؤ هلك» (Qurʾān 4:176 has «إن»).
- **book p.٢٣٣ fn ١**: «النائب مناب الفعل» — sense suggests «الفاعل».
- **book p.٢٣٤ fn ٥**: «عيسى ابن عمرو» (usually ʿĪsā ibn ʿUmar).
- **book p.٢٣٥ matn**: «فهي يكون». **book p.٢٣٦**: «إصطلاح»; fn ٥ «لا حذر» (perhaps «لأحذر»).
- **book p.٢٣٧ matn**: «إيك والأسد» for «إياك»; «وان تحذف».
- **book p.٢٣٩ fn ٤**: «إلي المكان». **book p.٢٤٠ fn ١**: «ذري»; «كان معين» for «كل معين».
- **book p.٢٤١ fn ١**: «فعلا» translated as the pattern «فعولا».
- **book p.٢١٣**: the Qurʾān reference for «رب احكم» (21:112) is the translator's, not printed.
- Page numbers on book pp.٢٢٢–٢٢٣ are blurred; read ٢٢٢ and ٢٢٣ from the sequence.

## Batch 6 (book pp.٢٤٢–٢٩١, read at high DPI, no diacritics)

Printed ٢٤٢–٢٩١. All marker/footnote counts balance. Clear in print but odd or
likely misprinted (transcribed as printed, `# REVIEW:` in the file):

- **book p.٢٤٢ fn ٤**: «يرد عليه بعد أعجبني التأديب» — «بعد» perhaps «نحو».
- **book p.٢٤٤ fn ٨**: «علة العقود» for «القعود»; «بعد الجبن» perhaps «يعد».
- **book p.٢٤٥ fn ١**: «فبالوجود» — sense unclear, perhaps «فبالأولى».
- **book p.٢٤٦ fn ٩**: second «مصاحبة» read as «مصاحبه».
- **book p.٢٤٧ matn**: «و«زيدا» بالرفع» — accusative printed where nominative is described.
- **book p.٢٤٨ fn ١**: «أعمال العامل» for «إعمال».
- **book p.٢٤٩**: fn ١ «جاز التعريف» (sense suggests «التفريق»); fn ٢ «وعمر راكبا».
- **book p.٢٥١ fn ٥**: «الفظي» for «اللفظي». **book p.٢٥٣**: fn ٦ «فعلى»; fn ٧ «الاشتهار»، «أبله» for «إبله»; fn ٨ «الزوج» for «الذود».
- **book p.٢٥٤**: fn ١ «يذددها»; fn ٢ «مضاف مجهول» (probably «مضارع»); fn ٧ «معركة» vs matn «معتركة».
- **book p.٢٥٥ fn ٥**: «فإنه لأضيافنا» — sense unclear.
- **book p.٢٥٨ fn ٥**: «جاء زيدا أسدا». **book p.٢٦١ fn ٣**: «انتهى» for «انتفى» (twice).
- **book p.٢٦٤ fn ١**: «من إن» for «من أن». **book p.٢٦٦ matn**: «وزراع» vs earlier «ذراع».
- **book p.٢٦٧ fn ٢**: «يسبع داخله بالقار» — perhaps «يسيع» (coat with pitch).
- **book p.٢٦٨**: «للتقليل والكثير» for «للقليل»; fn ٤ «وإن أخذهما» for «وأن أحدهما».
- **book p.٢٦٩ fn ٣**: «نظرا» for «نظر».
- **book p.٢٧٠**: fn ٣ «ولهذ»; fn ٤ «وهكذا وينبغي».
- **book pp.٢٧١–٢٧٢ matn**: «المنتصف» for «المنتصب». **book p.٢٧٢ matn**: «أورد مثنى» apparently omitted.
- **book p.٢٧٤ matn**: «طاب زيدا أبا» for «زيد». **book p.٢٧٥ fn ٤**: «أو مفعول» omitted (supplied in English).
- **book p.٢٨١**: fn ٢ «يعني غناء» (sense «يغني»); fn ٥ «احتيار» for «اختيار».
- **book p.٢٨٢ fn ٣**: «للنحوى». **book p.٢٨٣**: fn ٤ «وأي»; fn ٥ stray question mark.
- **book p.٢٨٧ matn**: «وعلى تقدير «إن»» — perhaps «أن».
- **book p.٢٩١ fn ٦**: «غير المنصوب منها أقل» — the matn says the reverse.
- **book p.٢٦٧ matn**: «جلستين» occurs twice, printed jilsatayn then jalsatayn; without
  vowels the Arabic is identical, so only the English distinguishes them.

## Batch 7 (book pp.٢٩٢–٣٤١, read at high DPI, no diacritics)

Printed ٢٩٢–٣٤١. All marker/footnote counts balance. Clear in print but odd or
likely misprinted (transcribed as printed, `# REVIEW:` in the file):

- **book p.٢٩٢ fn ٦**: stray hamza «إلىءأن» — written «إلى أن» (typesetting slip, flagged).
- **book p.٢٩٣ matn**: «هذه الصورة الست» for «الصور».
- **book p.٢٩٤**: fn ٨ «يحكم المماثلة» (sense «بحكم»); fn ١٠ «إن خبر» for «أن».
- **book p.٢٩٥ fn ٢ / 298 fn ٤**: «مضي الخبر» — sense unclear. **book p.٢٩٥ fn ٤**: «وعند سيبويه» contradicts the next sentence (perhaps «عند غير سيبويه»).
- **book p.٢٩٨**: matn «إن مثل» for «أن»; fn ٤ «سورة الإضافة» for «صورة».
- **book p.٢٩٩ fn ١**: «يتسر» for «يتيسر». **book p.٣٠٠ fn ١**: «وألحق» read as «والحق».
- **book p.٣٠١**: fn ٢ «بالياء الزائدة» (sense «بالباء»); fn ٤ «بين الجمع» (perhaps «الجميع»).
- **book p.٣٠٢**: fn ١ «حجر سابقه» unclear; fn ٦ «أتانا رجلة سرعة وبطأ»; fn ٧ «يتوقف عن الجر».
- **book p.٣٠٥ fn ٦**: «يتسعمل» for «يستعمل».
- **book p.٣٠٨ matn**: «للأدني»; «لا نسلم إن». **book p.٣٠٩ fn ١**: gloss on «العير» speaks of a bāʾ.
- **book p.٣١٠ matn**: «بـ«ثم»» vs lemma «ومن ثمة». **book p.٣١١**: matn «الأعشي»; fn ٢ argument looks odd.
- **book p.٣١٢**: lemma «الماءة» vs «المائة»; fn ١ «ليسدل»; fn ٦ «الحجر» (perhaps «الجر»); fn ٩ «للمدوح»، «بتعبد»، «الحديثان النتائج».
- **book p.٣١٣ matn**: «وهذا الاشتراك بين…» — a negation seems needed; English adds "[is lacking]".
- **book p.٣١٤ matn**: «الضاربك» (sense «ضاربك»); «ضاربك ك»; «بالام».
- **book p.٣١٩ fn ٣**: «لاستقالها» for «لاستقلالها».
- **book p.٣٢٠**: fn ٣ «لأجراء»; fn ٨ «أو فيقال»، «حمى». **book p.٣٢١ fn ٢**: «بمعنى» (perhaps «بمنى»).
- **book p.٣٢٢**: fn ١ «أدني»; matn missing opening guillemet. **book p.٣٢٣**: matn «الأسماء الأجناس»; fn ٨ garbled.
- **book p.٣٢٤ fn ٦**: «المنصوب» vs matn «المنسوب». **book p.٣٢٦ fn ٤**: «بين النعت،» lacks its second term.
- **book p.٣٢٨ fn ١**: «كان ما سواك هزل» (nominative predicate). **book p.٣٢٩ fn ٩**: «للمتعلقه».
- **book p.٣٣٠ fn ٥**: «رجل عدل» printed twice. **book p.٣٣٢**: fn ٣ «حاجته المتكلم»; fn ٥ «الاستعال».
- **book p.٣٣٥**: fn ١ «فلا تمل» (perhaps «فتأمل»); fn ٥ «فكأنه فيه تجريدا».
- **book p.٣٣٦ matn**: «بتوسط» vs «يتوسط». **book p.٣٣٨ matn**: «متسايان».
- **book p.٣٣٩**: fn ٣ «أعجبتني جمالك» vs matn «أعجبني»; fn ٥ «نعم قابليته الإعراب كذلك».
- **book p.٣٤١**: fn ١ «يسند جواز»; fn ٢ «فليغرب»; matn «الذي إذا يطير فيغضب» (standard example has no «إذا»).
- **book p.٣٢٧**: the Qurʾān reference for «نفخة واحدة» (69:13) is the translator's, not printed.

## Batch 8 (book pp.٣٤٢–٣٩١, read at high DPI, no diacritics)

All marker/footnote counts balance. Clear in print but odd or likely misprinted
(transcribed as printed, `# REVIEW:` in the file):

- **book p.٣٤٣ matn**: a clause printed twice («فإنه كثيرا ما ينسب الفعل…»); «لإفراده»/«لأفراده»; «وأفادتها» vs fn ٢ «وإفادتها»; fn ١ «إن جاء القوم» for «أن».
- **book p.٣٤٤ matn**: «أبصع» vs fn ٦ «أبضع» (both spellings may be intended).  <!-- key found on 4 pages -->
- **book p.٣٤٧ fn ١**: «أن يقول، فتأمل فاعرف» — what he should say is missing; matn «إلي المتبوع» (also on the next page).
- **book p.٣٤٨ fn ٢**: «يؤتيى» for «يؤتى».
- **book p.٣٥١ fn ١**: «فإنها المبدل منه» — sense unclear.
- **book p.٣٥٢ matn**: closing guillemet with no opening one; marker ٢ after «صدق صدق», though fn ٢ comments on «فجعل إذا قال».
- **book p.٣٥٣ fn ٢**: «بنتفسه» for «بنفسه».
- **book p.٣٥٤ fn ٦**: «والمسكور» for «والمكسور».
- **book p.٣٥٥ matn**: «هذا الألقاب» for «هذه»; fn ٥ «مبنى الأصل».
- **book p.٣٥٦ fn ٤**: two Qurʾān phrases with no evident link to the argument.
- **book p.٣٥٧ continued footnote**: closing clause on «الهمزة مع النون» — link to the argument unclear.
- **book p.٣٥٨ fn ١**: «كان لفظ العدل متقدم» for «متقدما».
- **book p.٣٥٩ matn**: paradigm begins «إننه» (for «إنني»); third-person forms missing.
- **book p.٣٦١ fn ٣**: «وقال الآن» — speaker not named.
- **book p.٣٦٢ matn**: «والزيدان ضاربتان» for «ضاربان».
- **book p.٣٦٥ matn**: «إجتماعهما»; «أوردته منفصلا» — sense requires «متصلا»; fn ٨ «في باب «أعلمت»» (perhaps «علمت»).
- **book p.٣٦٦ matn**: «المخاطبن»; «على الأخر».
- **book p.٣٦٨ matn**: «لتقي أخر المضارع».
- **book p.٣٦٩ matn**: «لنقل التضعيف» for «لثقل»; fn ٦ «بين الجمع» (perhaps «الجميع»).
- **book p.٣٧٠ fn ٢**: «نعتا وخبر التوسط» (expected «وخبرا»).
- **book p.٣٧٢ fn ١**: «لانتفضت» for «لانتقضت».
- **book p.٣٧٤ fn ١**: «سورة فاطر: ١٣، ٦، ٦٢، ٦٤» — the last three are al-Zumar 39:6 and Ghāfir 40:62, 64 (translator's reference added); fn ٤ «وهى».
- **book p.٣٧٥ matn**: «فهي ليس» for «ليست»; fn ٥ «لأنه المعرفة» for «لأن».
- **book p.٣٧٧ fn ٨**: «الاختمال» for «الاحتمال»; «الرضى»; fn ٦ lemma «وأما عداها» vs matn «وأما ما عداها».
- **book p.٣٧٨ fn ١**: «من أن البيان تمام بدون التام» — obscure.
- **book p.٣٧٩ fn ١**: «الشرطة» for «الشرطية»; fn ٥ «بعرفه» for «يعرفه».
- **book p.٣٨٠ fn ٢**: «موضوف» for «موصوف».
- **book p.٣٨١ matn and fn ٦**: the Qurʾān 29:62 quotation omits «من عباده»; fn ٤ «زائدة «إذ» بعده موصول» read as the causal «إذ».
- **book p.٣٨٢ matn**: «وهو محل في المفعول»; fn ٢ «مفروغا عنها»; fn ٥ «ولم يكن أن يكون» (sense «يمكن»).
- **book p.٣٨٣ fn ٢**: «الضاربة أنا زيد» (the example needs «الضاربه»).
- **book p.٣٨٤ matn**: «فيبقي».
- **book p.٣٨٥ fn ٥**: «مقامهن»; fn ٦ «محتاجة» — the sense of «تامة» requires «غير محتاجة»; fn ٨ «اختلفت».
- **book p.٣٨٨ fn ٣**: «كأن هذه» vs fn ٤ «كان هذه».
- **book p.٣٨٩ matn**: stray dot in «به.«تضجرت» (not transcribed); fn ٣ «ولما يستعمل فيه قط» (perhaps «فقط»).
- **book p.٣٩١ matn**: stray full stop before «أما».

## Batch 9 (book pp.٣٩٢–٤٤١, read at high DPI, no diacritics)

All marker/footnote counts balance. Clear in print but odd or likely misprinted
(transcribed as printed, `# REVIEW:` in the file):

- **book p.٣٩٢ matn**: «في أخره» (lemma has «آخره»); fn ٣ malformed first letter of «فيه» read as «فيه».
- **book p.٣٩٣ matn**: «ما كان باقية» (masculine verb, feminine predicate).
- **book p.٣٩٥ fn ١**: «ونصر ماضي التفضيل» (expected «التفعيل»).
- **book p.٣٩٧ fn ٢**: «يحاذبه» (the translator reports al-Qāmūs has «يجاذبه»; not checked); matn quotation marks unbalanced around «اثنى عشر».
- **book p.٣٩٨ fn ١**: «كم رجل كريم إياه هذا» — sense of «إياه» unclear; fn ٢ «يتسعمل» for «يستعمل»; fn ٣ «نبت» (expected «بنت»), «زيته».
- **book p.٣٩٩ fn ١**: «فرع الذي يتحقق معه العامل» — a noun seems missing; fn ٥ «تميزا»; «كم» الاستفهامية (sense requires «الخبرية»).
- **book p.٤٠٠ fn ٧**: «الإنساء» for «الإنشاء».
- **book p.٤٠١ fn ٣**: «من معمولا «لا» إلى اقتضاء الفعل» — odd; fn ١ «فالاستفهامية» (perhaps «في»).
- **book p.٤٠٢ fn ٢**: «نظير الأمثال» (perhaps «الأمثلة»).
- **book p.٤٠٣ matn**: «مختصتين» (expected «مختصتان»).
- **book p.٤٠٤ fn ٣**: «تنظير الحذف هذا المميز» (perhaps «لحذف»).
- **book p.٤٠٧ matn**: «مضافة الجملة» (expected «مضافة إلى الجملة»).
- **book p.٤٠٨ fn ١**: opens «الحكم ببناء؛ إذ استدلال…» — elliptical; «فالقول قولهم وإن جرد…» awkward.
- **book p.٤٠٩ continued footnote**: hemistich «إذ الخصم أبزى…» with «إذ» for «إذا»; fn ٣ «الفجأة»/«الفجاءة» spellings swapped.
- **book p.٤١٠ fn ٣**: «عدم بنائها ظرفية» (context suggests «بقائها»); unnumbered paragraph after fn ٦ «لتنزيل المستقل» for «المستقبل».
- **book p.٤١١ matn**: «أني زيد؟» with dotted yāʾ; fn ٢ «بيننا» (perhaps «بينا»), «وفي الباب وهما يعني» elliptical; fn ٦ sentence on «كيف» — link unclear.
- **book p.٤١٢ fn ٤**: examples «مذ اليوم» / «مذ الليلة» — assignment to past/present looks reversed.
- **book p.٤١٣ fn ٤**: «فيأبى عنه لفظة، فيليهما» (expected «لفظه:»).
- **book p.٤١٤ fn ٤**: «رحمه الله عليه» (expected «رحمة»); «فإن لما قبلهما مضافان» odd.
- **book p.٤١٥ fn ١**: «ويريد عليه» (expected «ويرد»).
- **book p.٤١٦ fn ٢**: «بحذف … تارة، ويثبت أخرى» (parallel suggests «يحذف»); fn ٧ a hamza-like mark in «الاستغراقية» — written plain (flagged).
- **book p.٤١٨ continued footnote**: «ولا وجود للاحتمال الثاني» — the non-occurring case should be the third.
- **book p.٤١٩ fn ١**: «المهمات» for «المبهمات»; fn ٣ «وقال الواضع» odd (both confirmed at 800 dpi).
- **book p.٤٢١ matn**: «والمهبمات» for «والمبهمات»; fn ٤ «أبو العتابية» (for «العتاهية»), «إسماعيل بن سويد».
- **book p.٤٢٣ fn ١**: «وكل انثني منها» (for «اثني»); closing sentence on «الكم الحكمي» unclear.
- **book p.٤٢٤ fn ٣**: «لكان امتزاجيا» read as «مكان».
- **book p.٤٢٥ fn ٤**: «موردا للجزء الثاني» — sense unclear.
- **book p.٤٢٦ fn ٤**: «عطف القعود» for «العقود».
- **book p.٤٢٧ matn**: «المعطوف إليه» (expected «عليه»); stray dot «التركيب،.لم» (omitted); fn ٣ «والحق التثنية» (perhaps «وألحق»).
- **book p.٤٢٨ fn ٤**: «مجيئة» for «مجيئه».
- **book p.٤٢٩ fn ٦**: «من يضيف عشرون «من» وأخواتها»; matn «ثلثمائة» (older spelling).
- **book p.٤٣٠ fn ٢**: verse ends «والضاءة» (usually cited «والفتاء»; not verified); fn ١ «مآت».
- **book p.٤٣١ fn ٤**: «ثنتا رجل حنظل» (the verse is usually «ثنتا حنظل»).
- **book p.٤٢٤ fn ٤**: «تلك المعدود»; stray mark before «إلى» (omitted).
- **book p.٤٣٣ fn ٣**: «الجمور» for «الجمهور»; fn ١ «المستثنى» (perhaps «المثنى»), «واحد ف مرتبة»; matn small mark over «سواء» (omitted).
- **book p.٤٣٤ fn ٥**: «للمؤنت» for «للمؤنث».
- **book p.٤٣٦ fn ٤**: «وقع فصل أولا» read as «أو لا».
- **book p.٤٣٩ fn ١**: «عوض من لحوق» (twice) — sense odd, confirmed at zoom.
- **book p.٤١٣ fn ٤**: «مقصودا» for «مقصورا».
- **book p.٤٤١ fn ٤**: «الغريقة» (fn ٢ has «العريقة»); matn «ألوان»/«ألي» vs fn ١ «إلوان»/«إلى».

## Batch 10 (book pp.٤٤٢–٤٩١, read at high DPI, no diacritics)

All marker/footnote counts balance. Generated from the `# REVIEW:` comments in
the page files (each is clear in print but odd or likely misprinted, and is
transcribed as printed):

- **book p.٤٤٢**: printed «وحكي المبرد» (final dotted yāʾ), whereas the parallel clause above has «وحكى أبو علي»; transcribed as printed, translated as «وحكى».
- **book p.٤٤٣**: printed «أخر» (without madda); read as «آخر» (“end”).
- **book p.٤٤٤**: printed «الإفراد» (kasra-form, “singularity”); context calls for «الأفراد» (“individuals”); transcribed as printed, translated as «الأفراد».
- **book p.٤٤٤**: printed «حاملين»; the parallel matn on printed ٤٤٥ has «جامل» (camel herd), so «جاملين» may be intended; transcribed as printed.
- **book p.٤٤٧**: printed «مستوفى» (here and in the third condition); context requires «مستو» (“sharing equally”, cf. the matn’s «مستويا فيه» below); transcribed as printed, translated in that sense.
- **book p.٤٤٧**: printed «مذكور» (after «الاسم المذكور»), where context suggests «مذكرا»; transcribed as printed.
- **book p.٤٤٧**: printed «العملية»; context (contrast of ʿalamiyya and waṣfiyya) suggests «العلمية»; transcribed as printed, translated as «العلمية».
- **book p.٤٤٨**: printed «يستوي فيه المذكر المؤنث» without the conjunction «و»; transcribed as printed, translated as «المذكر والمؤنث».
- **book p.٤٤٨**: printed «ولعل ذلك الاعتدال الكسر»; «لاعتدال» (“because of the balance”) seems intended; transcribed as printed.
- **book p.٤٤٨**: printed «كجقة» (two dots above the third letter); probably a misprint (e.g. for «جفنة»); transcribed as printed, left untransliterated in the English.
- **book p.٤٤٨**: printed «كسعة» as the example of an adjective on faʿl; «سعة» is not an obvious adjective of that measure; transcribed as printed.
- **book p.٤٤٩**: a small stray mark (a circle-like dot) is printed between «الصحيح» and marker [١]; ignored.
- **book p.٤٥١**: printed «كتب الصريف»; the expected word is «التصريف» (cf. «علم التصريف» below). Transcribed as printed, translated as «التصريف».
- **book p.٤٥١**: printed «بخلافه اسم الفاعل»; the expected form is «بخلاف اسم الفاعل». Transcribed as printed, translated as «بخلاف».
- **book p.٤٥٢**: the verse is printed vocalized as dhikru raḥmati rabbika ʿabdahu Zakariyyā (fatḥa on the dāl of «عبده», no hamza on «زكريا»), yet the note says the reading has «بضم الدال والهمزة»; the vowelling as printed does not show the reading described. Diacritics removed per the no-diacritics rule; translated as printed.
- **book p.٤٥٣**: printed «إذني زيد بقوله ذلك» (a clear print, no space after the colon); the form «إذني» is odd, perhaps for «أذاني» or «آذنني». Transcribed as printed; the English renders the sense tentatively.
- **book p.٤٥٤**: printed «كالزيادة فيهن» (feminine plural pronoun); the expected form is «فيه». Transcribed as printed, translated as «فيه».
- **book p.٤٥٤**: printed «بناء على أن الضمير «يرد» إلى أقرب المذكورات» with «يرد» in guillemets; the guillemets look misplaced (the sense is "the pronoun is referred to the nearest of the things mentioned"). Transcribed as printed.
- **book p.٤٥٤**: printed «كارمني فكرمته لكرمه»; the function of «لكرمه» here is unclear (the active participle would be «كارمه»/«كارم»). Transcribed as printed; English renders it literally.
- **book p.٤٥٥**: printed «أي: على زمنه»; the sense requires «على زعمه» ("according to his claim"). Transcribed as printed, translated as «زعمه».
- **book p.٤٥٥**: printed «ولم يكن في ذلك ضمير» ("pronoun"); the sense requires «ضير» ("harm"). Transcribed as printed, translated as «ضير».
- **book p.٤٥٧**: the page prints a stray dot after the colon («تعالى:.»); the dot is omitted here.
- **book p.٤٥٨**: printed «سورة الحج: ٣٨», but «لذائقوا العذاب» is Sūrat al-Ṣāffāt 37:38; transcribed as printed.
- **book p.٤٥٩**: the matn prints «الاخر» (bare alif, no madda); transcribed as printed.
- **book p.٤٦١**: a stray mark follows the colon in «أي:» on the first line; omitted here.
- **book p.٤٦٣**: printed «تعددا الفاعل» (with tanwīn-alif, printed with fatḥatān, before a definite noun); expected «تعدد الفاعل». Transcribed as printed (diacritics removed).
- **book p.٤٦٥**: printed «الصفة الشبهة»; expected «الصفة المشبهة». Transcribed as printed.
- **book p.٤٦٦**: printed «ذهاب حسن إحدى العينين»; one would expect «حس» (sense, sight). Transcribed as printed.
- **book p.٤٦٨**: the verse prints «ولست» (second person, as fn ٤ confirms: «على صيغة الخطاب»), but the gloss prints «ليست من بينهم». Transcribed as printed.
- **book p.٤٦٨**: printed «مع الأفعال الذي» (plural «الأفعال» with singular «الذي»); «أفعل» may be intended. Transcribed as printed.
- **book p.٤٦٨**: printed «فاستبقى» and «نحو جواز»; «جوار» (jawārin, with tanwīn in place of the yāʾ) may be intended. Transcribed as printed.
- **book p.٤٦٩**: printed «فيه إشارة إلا أن الأولى» and «بدل من إلا أنه»; «إلى أن» may be intended at least in the first place. Transcribed as printed.
- **book p.٤٦٩**: printed «غير الفضل عليه»; «المفضل عليه» expected. Transcribed as printed.
- **book p.٤٧٠**: printed «إلا لعموم أفعل»; the sense would lead one to expect «إلا بمعمول أفعل» (“except by what afʿal governs”). Transcribed as printed; translated literally.
- **book p.٤٧١**: printed «على نص عليه» (one would expect «على ما نص عليه» or «كما نص عليه»); also «وأن المراد بالضمير المستتر» seems to lack a predicate. Transcribed as printed; translated by sense.
- **book p.٤٧١**: printed «أنه لفظ لا أثر» — the sense is obscure (perhaps «أنه لا لفظ له لا أثر»); transcribed as printed, translated literally.
- **book p.٤٧٢**: printed «نقل عنه المشهور» (one might expect «عدل عن المشهور»); transcribed as printed, translated by sense.
- **book p.٤٧٣**: printed «هو هذا الوجه ذو الثاني» — «ذو» is odd here (perhaps for «دون»); transcribed as printed, translated by sense.
- **book p.٤٧٤**: printed «فانتفى لزائد أيضا» (one would expect «الزائد»); transcribed as printed.
- **book p.٤٧٤**: printed «فإن قوله: «في الجواب»، فإذا أزال بالنفي ينادي على فساده» — the quotation marks and punctuation are odd; transcribed as printed, translated by sense.
- **book p.٤٧٦**: footnote prints «وقوله: تطبيق» while the matn prints «ويطبق»; transcribed as printed in each place.
- **book p.٤٧٧**: printed «حذف الموصول» (the relative); the context (the qualified noun of «أحسن») suggests «الموصوف». Transcribed as printed, translated as «الموصوف».
- **book p.٤٧٨**: the two reformulations are printed identically («ولا أرى واديا أقل به ركب أتوه منه بوادي السباع»), although they are introduced as «العبارة الأولى» and «العبارة الثانية»; transcribed as printed.
- **book p.٤٧٩**: printed «حتى يراد» (and «صيغة المعنى»); the sense seems to call for «حتى يرد» (“so that the objection arises”). Transcribed as printed; translated by the apparent sense.
- **book p.٤٨١**: printed «أفاد التقييد في الإثبات الدخول» — the wording is unusual; transcribed as printed and translated literally.
- **book p.٤٨٤**: printed «إذ لبس الحروف مشابها بها» (لبس); the sense expected is «ليس». Transcribed as printed; translated as «ليس».
- **book p.٤٨٤**: printed «زيادتهما» (dual) referring to «الحروف», and «مع تفسير بعض الحركات», where «تغيير» would be expected. Transcribed as printed; translated as «تغيير».
- **book p.٤٨٥**: a stray full stop is printed after «واحدا كان» in mid-sentence («واحدا كان. أو مثنى»); transcribed as printed.
- **book p.٤٨٥**: printed «والمنؤنثين» (with an extra nūn) for «والمؤنثين»; transcribed as printed, translated as «المؤنثين».
- **book p.٤٨٦**: printed «احتراز عما هو أهل التصريف» (one would expect «عما هو عند أهل التصريف»); transcribed as printed.
- **book p.٤٨٨**: printed «علي أن» (with dotted yāʾ) for «على أن»; transcribed as printed.
- **book p.٤٨٨**: the matn opens with «(بـ«أن») ملفوظة» directly under the heading; the governing verb of the Kāfiya clause («وينتصب») is not printed here. Transcribed as printed.
- **book p.٤٨٩**: printed «الكفويين» for «الكوفيين»; transcribed as printed, translated as «الكوفيين».
- **book p.٤٨٩**: printed «معنى اللبيب» for the title «مغني اللبيب»; transcribed as printed.
- **book p.٤٨٩**: printed «لقول بزيادته» where «القول بزيادته» would be expected; transcribed as printed.
- **book p.٤٩١**: the opening guillemet before «أسلمت» has no printed closing guillemet; transcribed as printed.
- **book p.٤٩١**: printed «الأولى سواء كان أو ترك المستقبل فتدبر»; the sentence is elliptical as printed. Transcribed as printed; the translation follows the apparent sense.

## Batch 11 (book pp.٤٩٢–٥٤١, read at high DPI, no diacritics)

All marker/footnote counts balance. Generated from the `# REVIEW:` comments in
the page files (each is clear in print but odd or likely misprinted, and is
transcribed as printed):

- **book p.٤٩٣**: printed «فأما أدخل الآن»; the sense suggests «فأنا أدخل الآن» (so I am entering now). Transcribed as printed.
- **book p.٤٩٣**: printed «تقدير الجر منتفيا»; the context (the predicate of incomplete kāna) suggests «الخبر» (predicate). Transcribed as printed.
- **book p.٤٩٥**: printed «فأشربها» (feminine pronoun referring to «ماء»); transcribed as printed.
- **book p.٤٩٥**: printed «وما بعدها الفاء» (expected «وما بعد الفاء»); transcribed as printed.
- **book p.٤٩٥**: printed «اتق الله مرؤ»; the usual form of this example is «اتقى الله امرؤ». Transcribed as printed.
- **book p.٤٩٦**: printed «أي: إلا ترد»; the sense suggests «أي: ألا ترد» or «لا ترد». Transcribed as printed.
- **book p.٤٩٦**: printed «ليكن زيادة منك» (increase); the parallel gloss on the previous page reads «زيارة» (visit). Transcribed as printed.
- **book p.٤٩٦**: printed «لتقدير «إن»» (with kasra-hamza); the context concerns «أن». Transcribed as printed.
- **book p.٤٩٦**: printed «الجموع» and «أو فما قيل»; both are odd as printed (perhaps «المجموع»). Transcribed as printed; the translation follows the apparent sense.
- **book p.٤٩٧**: printed «لا خير»; the following «إنما الضرر» suggests «لا ضير» (no harm). Transcribed as printed.
- **book p.٤٩٨**: printed «الصراخ»; probably a misprint for «الصحاح» (al-Ṣiḥāḥ of al-Jawharī). Transcribed as printed.
- **book p.٤٩٩**: footnote ٢ prints «مضتمنة» (apparently for «متضمنة»); transcribed as printed.
- **book p.٤٩٩**: footnote ٣ prints «ولكمة» (apparently for «وكلمة»); transcribed as printed.
- **book p.٥٠٠**: footnote ١ prints «وإنما مدخول «إن لم أضرب»» (the quoted phrase includes «إن», which the sense suggests should be «لم أضرب»); transcribed as printed.
- **book p.٥٠٠**: footnote ٥ prints «فكان المصنف» and «وكان الشارح» (read in the sense of «فكأن»/«وكأن»); transcribed as printed.
- **book p.٥٠٢**: printed «وعلى كلا التقدير» (singular after «كلا»; one would expect «التقديرين»); transcribed as printed.
- **book p.٥٠٣**: the opening guillemet before «إن لا تكفر تدخل النار» has no printed closing guillemet; transcribed as printed.
- **book p.٥٠٥**: the clause «فإنه إذا قيل في: «أقتل» بكسر التاء» has no apodosis as printed; transcribed as printed.
- **book p.٥٠٥**: printed «بعده ضمه» (final hāʾ, apparently for «ضمة»); transcribed as printed.
- **book p.٥٠٧**: printed «احتماع» (with ḥāʾ), apparently a misprint for «اجتماع»; transcribed as printed, translated as «اجتماع».
- **book p.٥٠٨**: the printed heading reads «المعتدي» (letters transposed), apparently a misprint for «المتعدي»; transcribed as printed.
- **book p.٥٠٩**: printed «كالمعتدي» (letters transposed), apparently a misprint for «كالمتعدي»; transcribed as printed, translated as «كالمتعدي».
- **book p.٥١٠**: printed «عملت» in «فإن معنى عملت هذا زيدا», apparently a misprint for «علمت»; transcribed as printed, translated as «علمت».
- **book p.٥١١**: printed «يعطى» (alif maqṣūra) in «يعطى الفقراء», where the active «يعطي» is apparently intended; transcribed as printed, translated as active.
- **book p.٥١٢**: printed «هذه الإلغاء» (feminine demonstrative with a masculine noun); transcribed as printed. Also the matn prints «المنبيء» while footnote ٥ prints «المنبئ»; each transcribed as printed.
- **book p.٥١٢**: printed «وعامل لنصب» (without the article), apparently for «وعامل النصب»; transcribed as printed.
- **book p.٥١٣**: printed «إن زيد لقائم» (nominative زيد after إن); transcribed as printed.
- **book p.٥١٤**: printed «بقدر الامكان» here without hamza, while the same phrase is printed «الإمكان» elsewhere on this page; transcribed as printed.
- **book p.٥١٥**: the verse is printed «بضنين» (with ḍād), though it is cited as an instance of ظن «اتهم» and glossed «بمتهم» (the reading «بظنين»); transcribed as printed.
- **book p.٥١٥**: printed «حلقه» (with hāʾ), whereas footnote 1 has «الحلقة»; transcribed as printed.
- **book p.٥١٥**: printed «معاينها», whereas the commentary text has «معانيها»; transcribed as printed.
- **book p.٥١٧**: printed «موضوع التقرير الفاعل» (definite التقرير before الفاعل); transcribed as printed.
- **book p.٥١٩**: printed «كان يكون ناقصة» (masculine يكون, against «تكون» elsewhere); transcribed as printed.
- **book p.٥١٩**: printed «كقوله الشاعر» (pronoun suffix plus الشاعر); transcribed as printed.
- **book p.٥٢٠**: printed «ويكون في مقام الإيجاد وأيضا بمعنى كن موجودا»; the «و» before «أيضا» reads oddly. Transcribed as printed.
- **book p.٥٢١**: printed «مضارع» at the head of the note, although what follows lists the verbal nouns (بياتا، مبيتا، بيتوتة); likewise «ومضارع «ظل يظل»». Transcribed as printed.
- **book p.٥٢٢**: printed «إما دلالتها» where the sense calls for «أما»; transcribed as printed.
- **book p.٥٢٢**: printed «بجميع الخبر مع الفاعل»; «بجمع» may be intended. Transcribed as printed.
- **book p.٥٢٣**: printed «فما دام لم يشفع ما دام بـ«اجلس» ولم يحصل من المجموع كلام لا يفيد فائدة تامة»; the clause reads oddly (the sense seems to be: as long as «ما دام» is not joined to «اجلس» and no statement arises from the whole, it does not convey a complete benefit). Transcribed as printed; translation follows that apparent sense.
- **book p.٥٢٤**: printed «إلا أنه صرفة إلى الأفعال الناقصة» with tāʾ marbūṭa; «صرفه» (he directed it) seems intended. Transcribed as printed.
- **book p.٥٢٤**: printed «لعدم قولهم بتقدير "ما"»; «بتصدير» (head position) seems intended by the sense. Transcribed as printed; the translation follows the apparent sense.
- **book p.٥٢٦**: printed «لما يفضى إليه» with final ى here, but «فيما يفضي إليه» later in the same passage. Transcribed as printed.
- **book p.٥٢٦**: printed «موضوعة لدنو لخبر رجاء»; «لدنو الخبر» seems intended. Transcribed as printed.
- **book p.٥٢٦**: printed «فإنه لم يجيء» (with ي after «لم»); transcribed as printed.
- **book p.٥٢٧**: printed «إن زائدة» with hamza below the alif; the particle in question is «أن». Transcribed as printed.
- **book p.٥٢٩**: printed «لتخطئتم» (without the hā’ of «لتخطئتهم» as earlier in the sentence). Transcribed as printed.
- **book p.٥٣٠**: printed «يريها» in the Qur'anic quotation; the matn above and the Qur'an (24:40) read «يراها». Transcribed as printed.
- **book p.٥٣٠**: «ما سبق بدل على» printed; probably «يدل على»; transcribed as printed.
- **book p.٥٣١**: printed «والأشل عشرة»; the matn has «لا شل عشره» (apparently «ولا شل عشره» run together). Transcribed as printed.
- **book p.٥٣٢**: printed «كما له في الفضل تحققه» (with a space after «كما»); the sense may be «كماله في الفضل وتحققه». Transcribed as printed.
- **book p.٥٣٣**: printed «لأنه كان جهل»; the sense suggests «لأنه كأنه جهل». Transcribed as printed; the translation follows the apparent sense.
- **book p.٥٣٤**: printed «إحداهما» (dual) although four variants follow, and no preceding statement such as «وفيهما أربع لغات» is printed after the heading; transcribed as printed.
- **book p.٥٣٤**: printed «اتباعا» (hamzat al-waṣl) for the expected «إتباعا»; transcribed as printed.
- **book p.٥٣٥**: printed «أهل المصريين»; one would expect «أهل المصرين» (the people of the two cities, Baṣra and Kūfa). Transcribed as printed.
- **book p.٥٣٨**: printed «و«كأن» «قد» خرجت و«لما»» — no «و» between «كأن» and «قد», and «خرجت» stands outside the guillemets; read as the elliptical «كأن قد» and «خرجت ولما». Transcribed as printed.
- **book p.٥٣٩**: printed «ولا يصح على القدر من أول النهار إلى آخره»; «القدر» is clear but the phrase is elliptical. Transcribed as printed.

## Batch 12 (book pp.٥٤٢–٥٩٩, the end of the commentary, read at high DPI, no diacritics)

All marker/footnote counts balance. Generated from the `# REVIEW:` comments in
the page files (each is clear in print but odd or likely misprinted, and is
transcribed as printed):

- **book p.٥٤٢**: footnote 1 opens «ومعه وليس …» as printed; the sense of «ومعه» here is unclear (possibly «و"مع"» meant). Transcribed as printed.
- **book p.٥٤٣**: footnote 1 prints «اشترى الفرس» (verb form) where the sense seems to require «اشتراء الفرس» (the buying of the horse). Transcribed as printed.
- **book p.٥٤٤**: «لا ينبغي» is clearly printed; the argument seems to require «لا ينتفي» ("relative specification is not absent"). Transcribed as printed.
- **book p.٥٤٦**: «وكان المصنف» is printed; the sense seems to require «وكأن المصنف» ("it is as though the author"). Transcribed as printed.
- **book p.٥٤٧**: «وعند الكوفيون» is printed (nominative after «عند»); grammatically «الكوفيين» is expected. Transcribed as printed.
- **book p.٥٤٧**: «في وسط لكلام» is printed; «الكلام» is expected. Transcribed as printed.
- **book p.٥٤٩**: «بالله أجلس» is printed with hamzat al-qaṭʿ and fatḥa (with fatḥa on the alif); a request.
- **book p.٥٤٩**: «فصار مآله، ويجاب القسم» — punctuation as printed; sense is "its upshot became: the oath is answered".
- **book p.٥٤٩**: «أو أن» printed with hamza above the alif; the particle in the matn is «إن».
- **book p.٥٥١**: the sentence «ورجح الأول بأن الحكم بزيادة الاسم سيما إذا كان الحرف حرفا واحدا» appears.
- **book p.٥٥١**: «الأخفس والفاسي» printed thus; presumably for «الأخفش والفارسي» (al-Akhfash and.
- **book p.٥٥٢**: «كا إذا قلت» printed thus; presumably «كما إذا قلت». Transcribed as printed.
- **book p.٥٥٢**: «تفسير للمختصة» printed thus; the matn word is «المحضة». Transcribed as printed.
- **book p.٥٥٣**: «لكون كل منهما» printed with a dual pronoun although the referent is plural; transcribed as printed.
- **book p.٥٥٥**: «وسط كلامه المتكلم» printed thus (pronoun suffix with a following definite noun); transcribed as printed.
- **book p.٥٥٦**: printed «ليس فعلا» where the list (فاعلة، مفعولة…) suggests «فاعلا» — transcribed as printed.
- **book p.٥٥٦**: printed «غير معقول القول»; the context (and «غير مقول القول» two lines below) suggests «مقول» — transcribed as printed.
- **book p.٥٥٦**: the example «علمت أن زيدا قائم» is printed without the lām al-ibtidāʾ that the sentence describes (cf. «لقائم» in n. 4) — transcribed as printed.
- **book p.٥٥٧**: printed «إشارة إلا أنه»; «إلى» is expected — transcribed as printed.
- **book p.٥٥٧**: printed «جواب الآخر»; «جواز الآخر» is expected — transcribed as printed; translated by sense.
- **book p.٥٦٠**: printed «مستنكرا» (accusative) where «مستنكر» is expected as the predicate of «لأن كون…» — transcribed as printed.
- **book p.٥٦٣**: the full stop after «وإعمال المكسورة» is printed so, though the sentence runs on («بعد تخفيفها في سعة الكلام واقع»); transcribed as printed.
- **book p.٥٦٧**: printed «أيام الصباح» (al-ṣabāḥ, morning) where the verse just quoted has «الصبا» (youth); transcribed as printed.
- **book p.٥٦٧**: here and below «الصبى» is printed with alif maqṣūra, against «الصبا» in the verse; transcribed as printed.
- **book p.٥٦٨**: «أما أنهم بعض آخر» is printed so (the sense seems to be «أما أنه بعض آخر»); transcribed as printed.
- **book p.٥٦٩**: printed «أو وأما» (wa-ammā, with fatḥa and shadda) where the coordinating «إما» is meant; transcribed as printed (without diacritics).
- **book p.٥٦٩**: elliptical; the English adds a bracketed "[not]" to make sense of it — this inserted negation reverses the literal wording and needs checking.
- **book p.٥٦٩**: printed «بلا مهملة» (muhmala); the sense requires «مهلة» (delay); transcribed as printed.
- **book p.٥٧٠**: printed «ليس المراد بالإفادة في الخارج في الذهن»; a word such as «بل» seems missing before «في الذهن»; transcribed as printed.
- **book p.٥٧٠**: printed «قدم الحجاج»; the matn has «قدم الحاج»; transcribed as printed.
- **book p.٥٧٠**: printed «المهملة» for «المهلة»; transcribed as printed.
- **book p.٥٧١**: «وعدم الحاجة إلا أن يقال» — the sense of «وعدم الحاجة» is elliptical as printed; transcribed as printed.
- **book p.٥٧١**: printed «أما «لو» للتفصيل»; «لو» is unexpected here (one would expect «إما»); transcribed as printed.
- **book p.٥٧٢**: printed «فإنه لا يصح جوابهما بـ«لا و نعم»»; the argument and footnote ٥ require «يصح» (it is correct); transcribed as printed.
- **book p.٥٧٢**: printed «والمفرد أن بعدهما»; possibly for «والمراد»; transcribed as printed.
- **book p.٥٧٢**: printed «وربما بما يتوهم»; «بما» appears superfluous; transcribed as printed.
- **book p.٥٧٢**: printed «ما في عدم عده»; likely for «إنما في عدم عده»; transcribed as printed.
- **book p.٥٧٣**: printed «كان جوابا بالتعيين» (not «كون جوابها»); transcribed as printed.
- **book p.٥٧٤**: printed «لما قبل إلا» (expected perhaps «لما قبل لا») and «للمعطوف عليها»; transcribed as printed.
- **book p.٥٧٦**: printed «يكون إقرار» (grammatically «إقرارا» would be expected); transcribed as printed.
- **book p.٥٧٨**: "وارق السلم" here is printed identically to the verse line; the variant.
- **book p.٥٧٨**: «مثلثة وكعد» printed as such; the dictionary formula is likely «كعدو»; transcribed as printed.
- **book p.٥٨٠**: «تفسير الغير» printed as such (one expects «تفسيرا لغير»); transcribed as printed.
- **book p.٥٨٠**: «للظرفية للاعتبارات» printed as such (one expects «للظرفية الاعتبارية»); transcribed as printed.
- **book p.٥٨٢**: «ثم أنه» printed with hamza above the alif (one expects «ثم إنه»); transcribed as printed.
- **book p.٥٨٣**: the Qurʾānic «الإنسان» is printed in the Qurʾān font as alif with hamza above.
- **book p.٥٨٤**: footnote ٢ prints «هود: ٨», but «أفمن كان على بينة من ربه» is Hūd 11:17; transcribed as printed.
- **book p.٥٨٥**: printed «انتفاأين» and «الانتفاأين» (unusual spelling of the dual of «انتفاء»); transcribed as printed.
- **book p.٥٨٧**: printed «على تقدير توسطة» with final tāʾ marbūṭa (one would expect «توسطه»); transcribed as printed.
- **book p.٥٨٩**: printed «مهما يكن يزد فمنطلق» («يزد», apparently for «زيد»); transcribed as printed.
- **book p.٥٨٩**: printed «وحذف الفعل الشرط» (one would expect «فعل الشرط»); transcribed as printed.
- **book p.٥٩٢**: printed «وعرضوه» as transcribed; the sense requires «وعروضه» (its being accidental), translated so.
- **book p.٥٩٣**: printed «لئلا يبقى الكلمة» (masculine verb with the feminine «الكلمة»); transcribed as printed.
- **book p.٥٩٤**: printed «روى» (with alif maqṣūra), where «روي» is expected; transcribed as printed.
- **book p.٥٩٤**: printed «التجاوز عند الحد» where «عن الحد» is expected; transcribed as printed, translated by the sense.
- **book p.٥٩٤**: printed «يسقط عد التقطيع», where «عند التقطيع» is expected (or «عد» = counting); transcribed as printed.
- **book p.٥٩٤**: printed «لأن معناه الترنم» (because its meaning is chanting), which contradicts the.
- **book p.٥٩٧**: in the first paragraphs of this page the imperatives of غزا are printed with.
- **book p.٥٩٧**: printed «لم تروا القوم؟» with a question mark after a «لم» clause; transcribed as printed.
- **book p.٥٩٧**: the matn lemma «اغزن؟» and «واغزن؟» carry a question mark in print, though they are imperatives; transcribed as printed.
- **book p.٥٩٨**: printed «على الوقت», where «على الوقف» (on the pausal form) is expected; transcribed as printed, translated by the sense.
- **book p.٥٩٩**: «مكد الانتهاض» is clearly printed; «مكد» is read as the place of toil (from كد); rendered accordingly.

## Remaining minor points to verify against your print

- **book p.٢٣ footnote 6**: read as `عطف البيان والتفسير` (appositional explication);
  the scan glyph is slightly ambiguous — confirm it isn't `عطف الحذف`.
- **book p.٩١ footnote 7**: the word after `معدولاً` reads `صمت` at high zoom;
  semantically odd, transcribed faithfully.
- A handful of footnote-marker anchors where two notes gloss adjacent words were
  placed by sense; counts all balance.

Send any corrections and I will update the file(s) and rebuild.

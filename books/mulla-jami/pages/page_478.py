# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 478 (printed ٤٧٧)."""

PAGE_NUMBER = 478
PRINTED_PAGE = "٤٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أحسن فيها الكحل من» at the foot of PDF p. 477 (mid-sentence).
    {"type": "matn",
     "ar": "عين زيد»، أو تقول معناه: «ما رأيت عينا كعين زيد في كونها أحسن فيها الكحل منه في غيرها»،",
     "en": "…than in the eye of Zayd”; or you say that its meaning is: “I have not seen an eye like the eye of Zayd in its being one in which kohl is more beautiful than it is in any other”;"},
    {"type": "matn",
     "ar": "ويلزم من هذا على أبلغ وجه[[١]] أن للكحل في عين زيد حسنا ليس في عين غيره،",
     "en": "and from this it follows, in the most eloquent manner, that kohl has in the eye of Zayd a beauty it has not in the eye of anyone else."},
    {"type": "matn",
     "ar": "وإنما جازت هذه الصورة وإن لم يكن فيها فصل ظاهر لو رفعت «أفعل» بالابتداء؛ لأنها فرع الأولى،",
     "en": "This form is permitted, even though it has no evident separation [between the subject and the predicate] were you to put “afʿal” in the nominative as an inchoative (ibtidāʾ), only because it is a derivative of the first [form],"},
    {"type": "matn",
     "ar": "ولأن «من» التفضيلية مع مجرورها مقدرة فيها أيضا كما ذكرنا",
     "en": "and because the comparative “min” together with its genitive object is implied in it as well, as we have mentioned."},
    {"type": "matn",
     "ar": "(مثل: «ولا أرى») منصوب على أنه صفة مصدر محذوف أي: قلت: ما رأيت كعين زيد إلى آخره قولا يماثل قول الشاعر،",
     "en": "(Like: “wa-lā arā”): [mithl] is in the accusative as the adjective of an elided verbal noun (maṣdar), that is: you said “I have not seen [an eye] like the eye of Zayd…” to the end, a saying that resembles the poet’s saying."},
    {"type": "matn",
     "ar": "وإنما ترك صدر البيت ليكون مبتدأ بما هو في مبدأ للمماثلة،",
     "en": "He left out the opening of the line only so that it would begin with what stands at the starting point of the resemblance;"},
    {"type": "matn",
     "ar": "وترك موصوف «أحسن» في المثال وإن كانت المماثلة الكاملة في ذكره؛ إذ هو في مقابلة قوله: «واديا» وهو مذكور؛",
     "en": "and he left out the noun qualified by “aḥsan” in the example, even though complete resemblance lay in mentioning it, since it corresponds to the poet’s word “wādiyan”, which is mentioned,"},
    {"type": "matn",
     "ar": "لأنه كان في مقام بيان الاختصار[[٢]] في المثال المذكور أولا، وتمام البيت مع ما يليه:",
     "en": "because he was concerned with showing the abridgement in the example mentioned first. The whole line, with what follows it, is:"},
    {"type": "verse",
     "ar": "مررت على وادي السباع ولا أرى      كوادي السباع حين يظلم واديا",
     "en": "I passed by Wādī al-Sibāʿ, and I see no valley like Wādī al-Sibāʿ when it grows dark,"},
    {"type": "verse",
     "ar": "أقل به ركب أتوه تأية      وأخوف إلا ما وقى الله ساريا",
     "en": "in which riders who come to it linger less, nor one more fearful, save whom Allah protects, for a night traveller."},
    {"type": "matn",
     "ar": "كان أصله: «لا أرى واديا أقل به ركب منهم في وادي السباع»، فقدم «وادي السباع» واستغنى عن ذكره ثانيا،",
     "en": "Its origin was: “I see no valley in which riders linger less than they do in Wādī al-Sibāʿ”; then he placed “Wādī al-Sibāʿ” first and dispensed with mentioning it a second time."},
    {"type": "matn",
     "ar": "الركب: اسم جماعة الركبان[[٣]]، وهو مخصوص براكبي الإبل،",
     "en": "Al-rakb is a noun for a group of riders (rukbān), and it is restricted to those riding camels;"},
    {"type": "matn",
     "ar": "والتأية من «أيي أو أي» كالتحية من: «حيي أو حي» وهو: المكث والتأني،",
     "en": "al-taʾiyya is from “ayiya” or “ayya”, like al-taḥiyya from “ḥayiya” or “ḥayya”, and it means staying and lingering;"},
    {"type": "matn",
     "ar": "وساريا من «السرى»[[٤]] وهو: السير في الليل.",
     "en": "and sāriyan is from “al-surā”, which is travelling by night."},
    {"type": "matn",
     "ar": "فقوله: «لا أرى» إما من رؤية البصر، أو من رؤية القلب[[٥]].",
     "en": "So his words “lā arā” are either from seeing with the eye or from seeing with the heart."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لكونه معلوما بطريق الكناية؛ لأن نفي عين مماثلة لعين زيد في الأحسنية لازم لأحسنية كحل عين زيد،",
     "en": "Because it is known by way of allusion (kināya); for denying an eye that resembles the eye of Zayd in being more beautiful is a concomitant of the greater beauty of the kohl of Zayd’s eye,"},
    {"type": "pair",
     "ar": "ووجود اللازم يدل على الملزوم، فيكون كدعوى الشيء بالبينة.",
     "en": "and the existence of the concomitant points to what entails it; so it is like claiming a thing together with its proof."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «حذف الموصول» (the relative); the context (the qualified noun of «أحسن») suggests «الموصوف». Transcribed as printed, translated as «الموصوف».
    {"type": "pair",
     "ar": "وما ذكره أوفق بالمقام والأحسن أن يقال: نبه بذكر المثال والتمثيل بالشعر على جواز حذف الموصول وذكره.",
     "en": "What he mentioned fits the context better; but it would be better to say: by citing the example and illustrating it with poetry he drew attention to the permissibility of both eliding the qualified noun and mentioning it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: ليس بجمع. نبه على ذلك ليصح منه ما سيأتي من جعل ساريا صفة ركبان؛",
     "en": "He means: it is not a plural. He drew attention to this so that what is to come, making “sāriyan” an adjective of “rukbān”, would be valid on his part;"},
    {"type": "pair",
     "ar": "لأن اسم الجمع لا يجب تأنيث المسند إلى ضميره، ولا جمع صفته بخلاف الجمع.",
     "en": "for with a collective noun (ism al-jamʿ) it is not obligatory to make feminine what is predicated of its pronoun, nor to put its adjective in the plural, unlike a plural."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "واحتمال جعله من السراية على أن يكون صفة مصدر محذوف أي: أخوف خوفا ساريا إلى الهلاك على ما قيل ضعيف؛",
     "en": "The possibility of taking it from al-sirāya (spreading), so that it is the adjective of an elided verbal noun, that is, “more fearful with a fear that spreads to destruction”, as has been said, is weak;"},
    {"type": "pair",
     "ar": "لأن حقه التقديم على المستثنى حينئذ، فلذا لم يلتفت إليه.",
     "en": "for in that case it ought to come before the excepted term; that is why he paid no attention to it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهناك احتمال ثالث أبلغ بحسب المعنى، وهو جعل أرى مجهولا أي: أظن.",
     "en": "There is a third possibility, more eloquent in meaning: taking “arā” as passive (urā), that is, “I suppose”."},
    {"type": "pair",
     "ar": "ونفي الظن أبلغ من نفي الرؤية البصرية والعلمية، فتبصر، واعلم.",
     "en": "Denying supposition is more forceful than denying visual or cognitive seeing; so reflect, and know."},
]

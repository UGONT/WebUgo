barba.init({
    transitions: [{
      name: 'fade',
      once(data) {
        gsap.from(data.next.container, {
          opacity: 0,
          duration: 0.2
        });
      },
      leave(data) {
        return gsap.to(data.current.container, {
          opacity: 0,
          duration: 0.2
        });
      },
      enter(data) {
        gsap.from(data.next.container, {
          opacity: 0,
          duration: 0.2
        });
      }
    }]
  });